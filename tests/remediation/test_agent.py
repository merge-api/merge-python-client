# This file contains professional-grade, strictly-typed unit tests for the AssuranceAgent.

from __future__ import annotations

import unittest
from unittest.mock import ANY, MagicMock, patch

from merge.core.client_wrapper import SyncClientWrapper
from merge.remediation.agent import AssuranceAgent
from merge.remediation.errors import RefreshFailureError


class TestAssuranceAgent(unittest.TestCase):
    """A suite of unit tests for the AssuranceAgent."""

    mock_client_wrapper: MagicMock
    mock_on_success: MagicMock
    mock_on_failure: MagicMock
    agent: AssuranceAgent

    def setUp(self) -> None:
        """Set up a fresh agent instance and mocks before each test."""
        self.mock_client_wrapper = MagicMock(spec=SyncClientWrapper)
        self.mock_on_success = MagicMock()
        self.mock_on_failure = MagicMock()
        self.agent = AssuranceAgent(
            client_wrapper=self.mock_client_wrapper,
            on_success=self.mock_on_success,
            on_failure=self.mock_on_failure,
            check_interval_seconds=60,
            expiry_threshold_days=30,
        )
    
    @patch("merge.remediation.agent.threading.Timer")
    def test_start_schedules_first_run(self: "TestAssuranceAgent", mock_timer_cls: MagicMock) -> None:
        """Verify that agent.start() correctly schedules the first check cycle."""
        self.agent.start()
        self.assertTrue(self.agent.is_running())
        
        # Assert that a Timer was created with the correct interval and target function.
        mock_timer_cls.assert_called_once_with(60, self.agent._run_check_cycle)  # type: ignore[misc]
        mock_timer_cls.return_value.start.assert_called_once()

    @patch("merge.remediation.agent.threading.Thread")
    @patch("merge.remediation.agent.time.time")
    def test_check_cycle_identifies_expiring_token(
        self: "TestAssuranceAgent", mock_time: MagicMock, mock_thread_cls: MagicMock
    ) -> None:
        """Ensure the agent correctly identifies a token within the expiry threshold."""
        current_time = 1000000000  # Fixed timestamp for testing
        mock_time.return_value = current_time

        # Token expires in 15 days, which is within the 30-day threshold.
        expires_at = current_time + (86400 * 15)
        mock_store = {"expiring_token": {"expires_at": expires_at, "refreshed": False}}

        with patch("merge.remediation.agent.MOCK_CREDENTIALS_STORE", mock_store):
            # We call the protected method directly to isolate this unit of logic.
            self.agent._check_and_remediate_credentials()  # type: ignore[misc]

        # It should have detected the token and spawned a thread to remediate it.
        mock_thread_cls.assert_called_once_with(
            target=self.agent._attempt_refresh_with_retries, args=("expiring_token",)  # type: ignore[misc]
        )

    @patch("merge.remediation.agent.time.sleep")
    def test_successful_refresh_invokes_on_success_callback(
        self: "TestAssuranceAgent", mock_sleep: MagicMock
    ) -> None:
        """Verify that a successful token refresh triggers the `on_success` callback."""
        with patch.object(self.agent, "_mock_api_refresh_call") as mock_api_call:
            # We call the protected method directly to test the refresh logic.
            self.agent._attempt_refresh_with_retries("good_token")  # type: ignore[misc]

        mock_api_call.assert_called_once_with("good_token")
        self.mock_on_success.assert_called_once_with("good_token")
        self.mock_on_failure.assert_not_called()

    @patch("merge.remediation.agent.time.sleep")
    def test_non_retryable_failure_invokes_on_failure_immediately(
        self: "TestAssuranceAgent", mock_sleep: MagicMock
    ) -> None:
        """Test that a non-retryable error fails immediately without retries."""
        mock_store = {"bad_token": {"refreshed": False}}
        with patch("merge.remediation.agent.MOCK_CREDENTIALS_STORE", mock_store), patch.object(
            self.agent, "_mock_api_refresh_call"
        ) as mock_api_call:
            mock_api_call.side_effect = ValueError("non-retryable error")
            self.agent._attempt_refresh_with_retries("bad_token")  # type: ignore[misc]

        # The API should only be called once.
        mock_api_call.assert_called_once_with("bad_token")
        self.mock_on_success.assert_not_called()

        # The failure callback should be invoked with a RefreshFailureError.
        self.mock_on_failure.assert_called_once()
        self.assertIsInstance(self.mock_on_failure.call_args[0][1], RefreshFailureError)

    @patch("merge.remediation.agent.time.sleep")
    def test_retryable_failure_exhausts_retries_and_invokes_on_failure(
        self: "TestAssuranceAgent", mock_sleep: MagicMock
    ) -> None:
        """Test that a retryable error attempts to refresh 5 times before failing."""
        mock_store = {"flaky_token": {"refreshed": False}}
        with patch("merge.remediation.agent.MOCK_CREDENTIALS_STORE", mock_store), patch.object(
            self.agent, "_mock_api_refresh_call"
        ) as mock_api_call:
            mock_api_call.side_effect = ConnectionError("flaky connection")
            self.agent._attempt_refresh_with_retries("flaky_token")  # type: ignore[misc]

        # It should have been called 5 times (the configured max_retries).
        self.assertEqual(mock_api_call.call_count, 5)
        self.mock_on_success.assert_not_called()
        self.mock_on_failure.assert_called_once_with("flaky_token", ANY)

    @patch("merge.remediation.agent.threading.Timer")
    def test_shutdown_cancels_active_timer(self: "TestAssuranceAgent", mock_timer_cls: MagicMock) -> None:
        """Verify the shutdown method correctly cancels the agent's timer."""
        # Simulate an active timer on the agent instance.
        mock_timer_instance = MagicMock()
        self.agent._timer = mock_timer_instance  # type: ignore[misc]

        self.agent.shutdown()

        self.assertFalse(self.agent.is_running())
        # The key assertion: the timer's cancel() method was called.
        mock_timer_instance.cancel.assert_called_once()

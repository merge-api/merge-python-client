# test_sprint.py
# This is a standalone script to verify the work of Days 4-6.
# Place this file in the root of the repository, outside the `src` directory.

import os
import typing
import time
import logging
import sys
from merge.client import Merge
from merge.remediation.errors import RefreshFailureError
from merge.remediation.agent import JsonLogFormatter

# Read log level from environment variable. Default to INFO if not set.
LOG_LEVEL_STR = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_LEVEL_MAP = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
}
LOG_LEVEL = LOG_LEVEL_MAP.get(LOG_LEVEL_STR, logging.INFO)

# Configure structured JSON logging with the desired level.
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonLogFormatter())
# `force=True` is used to override any existing logger configuration.
logging.basicConfig(level=LOG_LEVEL, handlers=[handler], force=True)


class FailureEvent(typing.TypedDict):
    token: str
    error: str

# --- Day 6 DoD: Define our callback functions ---
# These prove the agent's extensibility.
success_events: typing.List[str] = []
failure_events: typing.List[FailureEvent] = []

def handle_success(token: str):
    # In a real app, this would increment a Datadog metric or log a success event.
    print(f"\n--- SUCCESS CALLBACK TRIGGERED for {token} ---")
    success_events.append(token)

def handle_failure(token: str, error: RefreshFailureError):
    # In a real app, this would trigger a PagerDuty alert.
    print(f"\n--- FAILURE CALLBACK TRIGGERED for {token} ---")
    failure_events.append({"token": token, "error": str(error)})


def main():
    print("-" * 60)
    print("--- Verifying 'Operation Guided Missile' - Days 4-6 Sprint ---")
    print("-" * 60)

    print("\n[Step 1] Initializing Merge client and enabling Assurance Agent...")
    client = Merge(api_key="YOUR_API_KEY", account_token="YOUR_ACCOUNT_TOKEN")
    
    # Enable the agent with a VERY short interval for testing.
    agent = client.remediation.enable_assurance(
        on_success=handle_success,
        on_failure=handle_failure,
        check_interval_seconds=3, # Check every 3 seconds
        expiry_threshold_days=20   # Flag anything expiring within 20 days
    )
    print("Agent enabled successfully.")
    
    print("\n[Step 2] Monitoring agent activity for 10 seconds...")
    print("         (Watch the JSON logs below for agent actions)")
    
    try:
        time.sleep(10)
    finally:
        print("\n[Step 3] Shutting down agent...")
        agent.shutdown()
        print("Agent shutdown complete.")

    print("\n" + "-" * 60)
    print("--- Verification Complete: Checking final state ---")
    print(f"Total Success Events Captured: {len(success_events)}")
    print(f"Total Failure Events Captured: {len(failure_events)}")
    
    # Final assertion to determine success or failure of the sprint
    if "token_expiring_soon" in success_events and len(failure_events) == 2:
        print("\n[SUCCESS] All expected events were captured. Sprint goals met.")
    else:
        print("\n[FAIL] Did not capture all expected success/failure events.")
        print("Expected: 1 success, 2 failures.")
        print(f"Actual: {len(success_events)} success, {len(failure_events)} failures.")

    print("-" * 60)


if __name__ == "__main__":
    main()


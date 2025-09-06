# A self-contained script to demonstrate the Assurance Agent in an E2E test.

from __future__ import annotations

import logging
import os
import signal
import subprocess
import sys
import time
import typing

from merge.client import Merge
from merge.remediation.agent import AssuranceAgent

# --- App Configuration ---
MOCK_API_BASE_URL = "http://127.0.0.1:5002"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

# --- Global State ---
agent_handle: typing.Optional[AssuranceAgent] = None


# A custom formatter to add color to the log output for readability.
class ColoredFormatter(logging.Formatter):
    """A logging formatter that adds color to log messages."""

    COLORS = {
        "SUCCESS_CALLBACK": "\033[92m",  # Green
        "FAILURE_CALLBACK": "\033[91m",  # Red
        "ENDC": "\033[0m",
    }

    def format(self, record: logging.LogRecord) -> str:
        log_message = super().format(record)
        # For our specific callbacks, find and replace the keyword.
        # This is a simple approach; a more robust one might inspect record attributes.
        for key, color in self.COLORS.items():
            if key in log_message:
                log_message = log_message.replace(key, f"{color}{key}{self.COLORS['ENDC']}")
        return log_message


# --- Logging Setup ---
def configure_logging() -> None:
    """Sets up readable, colored logging for the application."""
    handler = logging.StreamHandler(sys.stdout)
    # Use our new ColoredFormatter and a simpler log format
    formatter = ColoredFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logging.basicConfig(level=LOG_LEVEL, handlers=[handler], force=True)
    # Give httpx its own logger to reduce noise unless we're debugging
    logging.getLogger("httpx").setLevel(logging.WARNING if LOG_LEVEL != "DEBUG" else logging.DEBUG)


# --- Merge Assurance Callbacks ---
def on_refresh_success(account_token: str) -> None:
    """Callback for when a token is successfully refreshed."""
    # Log a plain string so the ColoredFormatter can process it.
    logging.info(f"SUCCESS_CALLBACK: Token '{account_token}' was refreshed.")


def on_refresh_failure(account_token: str, error: Exception) -> None:
    """Callback for when a token refresh fails."""
    # Log a plain string so the ColoredFormatter can process it.
    logging.error(f"FAILURE_CALLBACK: Token '{account_token}' failed. Error: {error}")


# --- Main Execution ---
if __name__ == "__main__":
    configure_logging()
    server_process = None
    
    # Use a context manager for the server process to ensure it's always cleaned up.
    try:
        logging.info("Starting mock API server...")
        server_command = [sys.executable, "e2e_test/mock_server.py"]
        server_process = subprocess.Popen(
            server_command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            preexec_fn=os.setsid
        )
        time.sleep(2) # Give the server a moment to start up
        
        if server_process.poll() is not None:
             raise RuntimeError("Mock server failed to start. Is the port already in use?")

        # Initialize the Merge client
        client = Merge(
            api_key="YOUR_API_KEY", 
            account_token="YOUR_ACCOUNT_TOKEN",
            base_url=MOCK_API_BASE_URL 
        )

        agent_handle = client.remediation.enable_assurance(
            on_success=on_refresh_success,
            on_failure=on_refresh_failure,
            check_interval_seconds=5, # Short interval for demo
            expiry_threshold_days=30,
        )

        logging.info("--- DEMO START: Agent running for 15 seconds. ---")
        time.sleep(15)
        logging.info("--- DEMO END ---")

    finally:
        if agent_handle:
            logging.info("Shutting down Assurance Agent...")
            agent_handle.shutdown()
        
        if server_process:
            logging.info("Stopping mock API server...")
            try:
                os.killpg(os.getpgid(server_process.pid), signal.SIGTERM)
                server_process.wait(timeout=5)
                logging.info("Mock API server stopped.")
            except (ProcessLookupError, OSError) as e:
                logging.warning(f"Could not kill mock server, it may have already exited. Error: {e}")
                
            stdout, stderr = server_process.communicate()
            if stderr:
                 # Don't log expected 'Address already in use' as an error if we catch it.
                if "Address already in use" not in stderr:
                    logging.error(f"Mock server stderr: {stderr.strip()}")


    logging.info("Demonstration complete.")

# A minimal Flask application to demonstrate a real-world integration
# of the Merge Assurance agent.

from __future__ import annotations

import atexit
import logging
import os
import sys
import threading
import typing

from flask import Flask, jsonify

from merge.client import Merge
from merge.remediation.agent import AssuranceAgent, JsonLogFormatter
from merge.remediation.errors import RefreshFailureError

# --- Globals ---
# This is a simple way to hold a reference to the agent for the shutdown hook.
agent_handle: typing.Optional[AssuranceAgent] = None
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

# --- Application Setup ---
def configure_logging() -> None:
    """Sets up structured JSON logging for the application."""
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonLogFormatter())
    logging.basicConfig(level=LOG_LEVEL, handlers=[handler], force=True)

def create_app() -> Flask:
    """Creates and configures the Flask application."""
    configure_logging()
    app = Flask(__name__)

    @app.route("/")
    def index() -> typing.Any: # type: ignore
        """A simple health-check endpoint."""
        is_running = agent_handle.is_running() if agent_handle else False
        return jsonify({
            "status": "running",
            "assurance_agent_active": is_running
        })

    return app
    
# --- Agent Management ---
def handle_success(token: str) -> None:
    """Callback for successful token refreshes."""
    logging.info({"message": f"SUCCESS_CALLBACK: Token '{token}' was refreshed.", "component": "SampleApp"})

def handle_failure(token: str, error: RefreshFailureError) -> None:
    """Callback for failed token refreshes."""
    logging.error({"message": f"FAILURE_CALLBACK: Token '{token}' failed.", "error": str(error), "component": "SampleApp"})

def start_assurance_agent() -> None:
    """Initializes the Merge client and enables the Assurance agent."""
    global agent_handle
    logging.info({"message": "Initializing Merge client for Assurance Agent.", "component": "SampleApp"})
    
    # In a real app, these would come from a secure config.
    client = Merge(api_key="FAKE_API_KEY", account_token="FAKE_ACCOUNT_TOKEN")
    
    agent_handle = client.remediation.enable_assurance(
        on_success=handle_success,
        on_failure=handle_failure,
        check_interval_seconds=10,  # Check frequently for demonstration
        expiry_threshold_days=20
    )

def shutdown_agent() -> None:
    """A graceful shutdown function to be called on application exit."""
    logging.info({"message": "Application shutting down. Stopping agent...", "component": "SampleApp"})
    if agent_handle and agent_handle.is_running():
        agent_handle.shutdown()
    logging.info({"message": "Agent shutdown complete.", "component": "SampleApp"})

# --- Main Execution ---
if __name__ == "__main__":
    app = create_app()
    
    # Register the shutdown hook. This is CRITICAL for production readiness.
    atexit.register(shutdown_agent)

    # Start the agent in a background thread so it doesn't block the web server.
    agent_thread = threading.Thread(target=start_assurance_agent, daemon=True)
    agent_thread.start()

    logging.info({"message": "Starting Flask server on http://127.0.0.1:5001", "component": "SampleApp"})
    app.run(host="0.0.0.0", port=5001)
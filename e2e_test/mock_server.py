# A stateful mock server that simulates the Merge API for E2E tests.

from __future__ import annotations

import logging
import sys
import typing
from datetime import datetime, timedelta

from flask import Flask, jsonify, request

# --- Server Configuration ---
HOST = "127.0.0.1"
PORT = 5002

# --- In-Memory "Database" ---
# This global state allows the server to remember changes, like a token refresh.
mock_db: typing.Dict[str, typing.Dict[str, typing.Any]] = {}

def reset_mock_db() -> None:
    """Resets the database to its initial state."""
    global mock_db
    now = datetime.now()
    mock_db = {
        "token_ok_1": {"expires_at": (now + timedelta(days=45)).timestamp(), "refreshed": False},
        "token_expiring_soon": {"expires_at": (now + timedelta(days=15)).timestamp(), "refreshed": False},
        # This token will fail on its first refresh attempt, then succeed.
        "token_retry_success": {
            "expires_at": (now + timedelta(days=20)).timestamp(),
            "refreshed": False,
            "attempts": 0,
        },
        "token_immediate_failure": {"expires_at": (now + timedelta(days=5)).timestamp(), "refreshed": False},
    }

# --- Logging Setup ---
# Configure a logger for the mock server
log = logging.getLogger("MOCK_SERVER")
log.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
# Silence the default Werkzeug logger to use our own.
logging.getLogger('werkzeug').setLevel(logging.ERROR)


# --- Flask App ---
app = Flask(__name__)

@app.route("/api/v1/credentials", methods=["GET"])
def get_credentials() -> typing.Any:
    """Returns the current state of credentials."""
    log.info("Request received for GET /api/v1/credentials")
    return jsonify(mock_db)

@app.route("/api/v1/refresh-token", methods=["POST"])
def refresh_token() -> typing.Any:
    """Simulates the token refresh logic."""
    data = request.get_json()
    token = data.get("account_token")
    log.info(f"Request received for POST /api/v1/refresh-token for token: {token}")

    if not token or token not in mock_db:
        return jsonify({"error": "Invalid Token"}), 404

    # --- Simulation Logic ---
    if token == "token_expiring_soon":
        # On success, update the DB to show the token is no longer expiring.
        mock_db[token]["expires_at"] = (datetime.now() + timedelta(days=60)).timestamp()
        mock_db[token]["refreshed"] = True
        log.info(f"Successfully refreshed '{token}'. It now expires in 60 days.")
        return jsonify({"status": "refreshed"}), 200

    if token == "token_retry_success":
        mock_db[token]["attempts"] += 1
        # Fail on the first attempt to simulate a transient network error.
        if mock_db[token]["attempts"] <= 1:
            log.info(f"Simulating retryable failure for '{token}'. Attempt #{mock_db[token]['attempts']}.")
            return jsonify({"error": "Service Temporarily Unavailable"}), 503
        else:
            # Succeed on the second attempt.
            mock_db[token]["expires_at"] = (datetime.now() + timedelta(days=60)).timestamp()
            mock_db[token]["refreshed"] = True
            log.info(f"Successfully refreshed '{token}' after {mock_db[token]['attempts']} attempts.")
            return jsonify({"status": "refreshed"}), 200

    if token == "token_immediate_failure":
        return jsonify({"error": "Invalid Refresh Token"}), 401
    
    # Default case for other tokens
    return jsonify({"status": "no_action_needed"}), 200

# --- Main Execution ---
if __name__ == "__main__":
    reset_mock_db()
    log.info(f"Starting Mock Merge API Server on http://{HOST}:{PORT}")
    # Use a production-ready server like Waitress for cleaner logs
    app.run(host=HOST, port=PORT)
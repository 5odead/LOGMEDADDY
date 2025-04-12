> ⚠️ **Disclaimer:**  
This tool is intended for educational purposes only. It should only be used in controlled environments with explicit permission. Unauthorized use is illegal and unethical.


# 🧠 LOGMEDADDY — Linux Keylogger & Exfiltration (for Red Team & Cybersecurity)


**LOGMEDADDY** is a lightweight keyboard input monitoring and log exfiltration tool designed for **cybersecurity research**, **red team exercises**, and **adversary simulation labs**.

This project demonstrates:

- Continuous keylogging on Linux systems, capturing every key press.
- Storing logs temporarily in memory, so they don’t stay on the hard drive.
- Sending the captured data securely via the Telegram Bot API.
- Operating quietly in the background with minimal traces, using threading and self-cleanup.


---

## 📌 Features

- ✅ **System-wide Key Logging**  
Captures keystrokes from your keyboard on a Linux system.

- ✅ **In-Memory Log Storage**  
Stores logs temporarily in memory (not on the hard drive) to avoid leaving traces.

- ✅ **Stealthy Operation**  
Runs quietly in the background, making it hard to notice.

- ✅ **Telegram Exfiltration**  
Sends the captured logs to a Telegram chat securely.

- ✅ **Auto-Cleanup**  
Deletes the log file after it's successfully sent, leaving no trace behind.


---

## 💡 How It Works

### **Keylogger:**
Captures keystrokes from a specified Linux input device (`/dev/input/eventX`) and stores them in a memory-based log file with timestamps.

### **Exfiltration:**
The exfiltration script uploads the captured log file to a Telegram chat using the `sendDocument` API. It retries if necessary and deletes the local log after successful upload.

---

## ⚙️ Example Usage

### **Clone the Repository:**

```bash
git clone https://github.com/5odead/LOGMEDADDY.git
cd LOGMEDADDY
```
### **Run the Keylogger:**
```bash
python3 keylogger.py
```
### **Run the Exfiltration Script:**
```bash
python3 exfiltration.py
```





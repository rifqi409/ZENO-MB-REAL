# ZENO-MB: Master Control Hub (by FM)

Welcome to **ZENO-MB**, an advanced multi-function C2 (Command & Control) botnet control hub built for educational purposes. Created by **FM (Front Man)**, this tool is designed to provide a powerful yet simple interface to manage your botnet operations inside a Termux/Linux environment.

🔧 **What is ZENO-MB?**  
ZENO-MB is a Python-based C2 (Command & Control) panel that allows you to:
- Scan for vulnerable IPs  
- Perform brute force login attempts  
- Send payloads or droppers to bots  
- Join remote bots to your C2  
- Monitor and control connected bots  
- Launch coordinated attacks

🧠 **Components**
1. `bot.py` → This is the server-side bot listener. It must be running to receive instructions.
2. `ZENO-MB.py` → This is the control panel used to send commands to the bots.

🚀 **How to Run ZENO-MB**

**Step 1: Start the Bot Listener**

Open **Tab 1** in your Termux or terminal:
```bash
python bot.py

you will see something like

Bot online di port 8080... Siap menerima perintah C2
 * Running on http://127.0.0.1:8080

do not exit that run,if you want to attack

Step 2: Open the Control Panel

Swipe right to open Tab 2 (new session), then run:

python3 ZENO-MB.py

Now you will see the menu:

🔥 ZENO-MB: MASTER CONTROL HUB 🔥
[1] Scanner IP Rentan
[2] Brute Forcer Login
[3] Loader Dropper Bot
[4] Join Bot ke C2
[5] Pantau & Kontrol C2 Panel
[6] Launch Attack


⚠️ Disclaimer
This tool is built for educational and ethical hacking purposes only. Use it in lab environments or on systems you have permission to test.

Respect the power you hold. Always hack responsibly.

— Developed with 🔥 by FM (Front Man)

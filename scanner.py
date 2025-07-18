# scanner.py - versi auto-scan mirip Mirai
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

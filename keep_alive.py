from flask import Flask
from threading import Thread
import requests
import time

app = Flask(__name__)  # ✅ Cambiato da '' a __name__

@app.route('/')
def home():
    return "🤖 AI Uncensored Ultra Bot – Online 24/7 🟢"

@app.route('/ping')
def ping():
    return "Bot alive and running 🟢", 200

@app.route('/health')
def health():
    return "OK", 200

# ✅ Aggiungi questo endpoint aggiuntivo per massima compatibilità
@app.route('/status')
def status():
    return "🟢 ONLINE", 200

def external_ping():
    """Ping all'URL di sviluppo Replit"""
    dev_url = "5f36462e-3d51-4ab7-b268-4338a477948a-00-rtqbzhxfi9dv.janeway.replit.dev/"
    
    # Prova diversi endpoint
    endpoints = ['/ping', '/health', '/status', '/']

    while True:
        for endpoint in endpoints:
            try:
                full_url = f"https://{dev_url}{endpoint}"
                response = requests.get(full_url, timeout=10)
                print(f"✅ Ping {endpoint} → Status: {response.status_code}")
                break  # Se uno funziona, esci dal loop
            except Exception as e:
                print(f"❌ Ping {endpoint} fallito: {e}")

        time.sleep(120)  # Ogni 2 minuti

def local_ping():
    """Ping locale - aspetta che il server sia pronto"""
    time.sleep(5)  # ✅ Aspetta 5 secondi che il server si avvii

    while True:
        try:
            response = requests.get("http://localhost:8080/ping", timeout=5)
            print(f"🔄 Ping locale → Status: {response.status_code}")
        except Exception as e:
            print(f"⚠️  Ping locale fallito: {e}")
        time.sleep(150)  # Ogni 2.5 minuti

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    # Avvia server Flask
    t = Thread(target=run)
    t.daemon = True
    t.start()
    print("🚀 Server Flask avviato su porta 8080")

    # Aspetta che il server sia pronto
    time.sleep(3)

    # Avvia entrambi i ping
    Thread(target=local_ping, daemon=True).start()
    Thread(target=external_ping, daemon=True).start()

    print("🔁 Sistema keep-alive MULTIPLO attivato!")
    print("💡 Bot rimarrà online con ping combinati")

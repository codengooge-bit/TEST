"""Mini serveur de pixel traceur — pour comprendre le mecanisme et tester sur soi-meme.

Sert une image 1x1 transparente et journalise IP, user-agent et date de chaque requete.

But educatif : comprendre comment fonctionne un "pixel espion" (tracking pixel)
pour mieux le reperer et s'en proteger dans ses propres emails.

⚠️ A n'utiliser que sur tes propres appareils/connexions, ou avec consentement
explicite. Envoyer ce lien a quelqu'un sans son accord pour capter son IP est
illegal (atteinte a la vie privee).

Usage:
    pip install flask
    python server.py
Puis ouvre http://localhost:5000/pixel.gif dans ton navigateur (ou depuis ton
telephone via l'IP locale / un tunnel ngrok) et regarde le fichier pixel_log.txt.
"""
import datetime

from flask import Flask, Response, request

app = Flask(__name__)

# GIF transparent 1x1 (invisible une fois insere dans une page ou un email)
PIXEL = bytes.fromhex(
    "47494638396101000100800000000000ffffff21f90401000000002c00000000010001000002024c01003b"
)

LOG_FILE = "pixel_log.txt"


@app.route("/pixel.gif")
def pixel():
    # X-Forwarded-For est renseigne quand on passe par un tunnel/reverse-proxy (ex: ngrok)
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.headers.get("User-Agent", "inconnu")
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")

    entry = f"{timestamp} | IP: {ip} | User-Agent: {user_agent}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print("[+] Pixel charge ->", entry.strip())

    return Response(PIXEL, mimetype="image/gif")


@app.route("/")
def home():
    return "Serveur de test actif. Charge /pixel.gif pour generer une entree de log."


if __name__ == "__main__":
    print("[*] Serveur lance sur http://localhost:5000")
    print("[*] Ouvre http://localhost:5000/pixel.gif puis consulte pixel_log.txt")
    app.run(host="0.0.0.0", port=5000)

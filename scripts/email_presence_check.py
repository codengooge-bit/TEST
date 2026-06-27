"""Vérifie où une adresse email a une présence publique (Gravatar, et optionnellement
Have I Been Pwned si tu as une clé API).

⚠️ N'utilise ce script que sur tes propres adresses email ou avec autorisation explicite.
Ne l'utilise pas pour traquer ou harceler quelqu'un.

Usage: python email_presence_check.py test@example.com
"""
import hashlib
import os
import sys

import requests


def check_gravatar(email: str) -> None:
    email_hash = hashlib.md5(email.strip().lower().encode("utf-8")).hexdigest()
    url = f"https://www.gravatar.com/avatar/{email_hash}?d=404"
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print(f"Gravatar      : profil trouvé -> https://www.gravatar.com/{email_hash}")
    else:
        print("Gravatar      : aucun profil trouvé")


def check_hibp(email: str) -> None:
    api_key = os.environ.get("HIBP_API_KEY")
    if not api_key:
        print("HaveIBeenPwned: ignoré (définis la variable d'env HIBP_API_KEY pour activer cette vérification)")
        return
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": api_key, "User-Agent": "OSINT learning script"}
    response = requests.get(url, headers=headers, timeout=5)
    if response.status_code == 200:
        breaches = [b["Name"] for b in response.json()]
        print(f"HaveIBeenPwned: trouvé dans des fuites -> {', '.join(breaches)}")
    elif response.status_code == 404:
        print("HaveIBeenPwned: aucune fuite connue")
    else:
        print(f"HaveIBeenPwned: erreur ({response.status_code})")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python email_presence_check.py <email>")
        sys.exit(1)

    target = sys.argv[1]
    check_gravatar(target)
    check_hibp(target)

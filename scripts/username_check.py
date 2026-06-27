"""Vérifie si un pseudo existe sur quelques sites publics (vérification basique du code HTTP).

À utiliser uniquement sur des pseudos vous appartenant ou avec autorisation.

Usage: python username_check.py monpseudo
"""
import sys
import time

import requests

SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter/X": "https://x.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Reddit": "https://www.reddit.com/user/{}",
}


def check(username: str) -> None:
    headers = {"User-Agent": "Mozilla/5.0 (OSINT learning script)"}
    for site, url_template in SITES.items():
        url = url_template.format(username)
        try:
            response = requests.get(url, headers=headers, timeout=5)
            status = "trouvé" if response.status_code == 200 else f"non trouvé ({response.status_code})"
        except requests.RequestException as exc:
            status = f"erreur ({exc})"
        print(f"{site:12} : {status}")
        time.sleep(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python username_check.py <pseudo>")
        sys.exit(1)
    check(sys.argv[1])

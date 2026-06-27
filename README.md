# Python OSINT — Guide débutant

Petit projet pour démarrer en Python et découvrir l'OSINT (Open Source Intelligence) de façon **légale et éthique**.

⚠️ **Règles importantes** : n'utilisez ces outils que sur des cibles pour lesquelles vous avez l'autorisation explicite (vos propres comptes, des labs de test, des CTF, ou avec consentement écrit). Ne harcelez jamais quelqu'un, ne contournez pas les protections de sécurité, et respectez les conditions d'utilisation des sites visités.

## Installation

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Scripts inclus

| Script | Description |
|---|---|
| `scripts/whois_lookup.py` | Récupère les infos WHOIS d'un nom de domaine |
| `scripts/dns_lookup.py` | Résout les enregistrements DNS (A, MX, TXT, NS...) d'un domaine |
| `scripts/email_format_check.py` | Vérifie si une adresse email est syntaxiquement valide |
| `scripts/username_check.py` | Vérifie la présence d'un pseudo sur plusieurs sites publics |
| `scripts/metadata_extractor.py` | Extrait les métadonnées EXIF d'une image |

## Pour aller plus loin

- Apprendre les bases Python (variables, fonctions, boucles) avant de complexifier.
- Étudier `requests`, `socket`, `dnspython`, `python-whois`, `Pillow`.
- S'entraîner sur des plateformes légales : TryHackMe (module OSINT), CTF dédiés OSINT.
- Lire la documentation officielle des outils OSINT reconnus (Maltego, theHarvester) pour comprendre les concepts, même sans les utiliser tout de suite.

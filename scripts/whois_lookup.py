"""Récupère les infos WHOIS publiques d'un nom de domaine.

Usage: python whois_lookup.py example.com
"""
import sys

import whois


def lookup(domain: str) -> None:
    info = whois.whois(domain)
    print(f"Domaine        : {info.domain_name}")
    print(f"Registrar      : {info.registrar}")
    print(f"Date création  : {info.creation_date}")
    print(f"Date expiration: {info.expiration_date}")
    print(f"Serveurs DNS   : {info.name_servers}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python whois_lookup.py <domaine>")
        sys.exit(1)
    lookup(sys.argv[1])

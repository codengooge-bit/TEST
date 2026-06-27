"""Résout les enregistrements DNS publics d'un domaine.

Usage: python dns_lookup.py example.com
"""
import sys

import dns.resolver

RECORD_TYPES = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]


def lookup(domain: str) -> None:
    for record_type in RECORD_TYPES:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            print(f"{record_type}:")
            for answer in answers:
                print(f"  {answer}")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            continue


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dns_lookup.py <domaine>")
        sys.exit(1)
    lookup(sys.argv[1])

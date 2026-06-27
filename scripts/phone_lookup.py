"""Récupère des infos publiques sur un numéro de téléphone : pays, opérateur, fuseau horaire.

⚠️ N'utilise ce script que sur tes propres numéros ou avec autorisation explicite.

Usage: python phone_lookup.py +33612345678
"""
import sys

import phonenumbers
from phonenumbers import carrier, geocoder, timezone


def lookup(number: str) -> None:
    parsed = phonenumbers.parse(number, None)

    print(f"Numéro valide   : {phonenumbers.is_valid_number(parsed)}")
    print(f"Pays            : {geocoder.description_for_number(parsed, 'fr')}")
    print(f"Opérateur       : {carrier.name_for_number(parsed, 'fr') or 'inconnu'}")
    print(f"Fuseau(x) horaire: {', '.join(timezone.time_zones_for_number(parsed))}")
    print(f"Format international: {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python phone_lookup.py <numero avec indicatif, ex: +33612345678>")
        sys.exit(1)
    lookup(sys.argv[1])

"""Vérifie si une adresse email est syntaxiquement valide (pas une vérification d'existence).

Usage: python email_format_check.py test@example.com
"""
import re
import sys

EMAIL_REGEX = re.compile(r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$")


def is_valid(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python email_format_check.py <email>")
        sys.exit(1)
    email = sys.argv[1]
    print(f"{email} -> {'valide' if is_valid(email) else 'invalide'}")

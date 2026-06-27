"""Extrait les métadonnées EXIF d'une image (ex: appareil photo, date, GPS si présent).

Usage: python metadata_extractor.py photo.jpg
"""
import sys

from PIL import Image
from PIL.ExifTags import TAGS


def extract(image_path: str) -> None:
    image = Image.open(image_path)
    exif_data = image.getexif()

    if not exif_data:
        print("Aucune métadonnée EXIF trouvée.")
        return

    for tag_id, value in exif_data.items():
        tag_name = TAGS.get(tag_id, tag_id)
        print(f"{tag_name}: {value}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python metadata_extractor.py <image>")
        sys.exit(1)
    extract(sys.argv[1])

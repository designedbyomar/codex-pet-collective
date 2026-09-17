#!/usr/bin/env python3
"""Validate the pet catalog and materialize its public Pages data and previews."""

from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "pets" / "catalog.json"
SITE_ROOT = ROOT / "site"
DATA_PATH = SITE_ROOT / "data" / "pets.json"
PREVIEW_ROOT = SITE_ROOT / "assets" / "pets"
MANIFEST_FIELDS = {"id", "displayName", "description", "spriteVersionNumber", "spritesheetPath"}
REQUIRED_CATALOG_FIELDS = {
    "id",
    "name",
    "description",
    "creator",
    "creatorUrl",
    "license",
    "path",
    "species",
    "actions",
    "preview",
    "featured",
}


def fail(message: str) -> None:
    raise SystemExit(f"Catalog build failed: {message}")


def main() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    if catalog.get("schemaVersion") != 2:
        fail("pets/catalog.json must use schemaVersion 2")

    pets = catalog.get("pets")
    if not isinstance(pets, list) or not pets:
        fail("catalog must contain a non-empty pets array")

    seen_ids: set[str] = set()
    featured = []
    public_pets = []
    if PREVIEW_ROOT.exists():
        shutil.rmtree(PREVIEW_ROOT)
    PREVIEW_ROOT.mkdir(parents=True, exist_ok=True)

    for pet in pets:
        missing = REQUIRED_CATALOG_FIELDS - set(pet)
        if missing:
            fail(f"{pet.get('id', '<unknown>')} is missing {', '.join(sorted(missing))}")
        pet_id = pet["id"]
        if pet_id in seen_ids:
            fail(f"duplicate pet id {pet_id}")
        seen_ids.add(pet_id)
        if not isinstance(pet["actions"], list) or not pet["actions"]:
            fail(f"{pet_id} must provide at least one action")
        if pet["featured"]:
            featured.append(pet_id)

        pet_dir = ROOT / pet["path"]
        manifest_path = pet_dir / "pet.json"
        atlas_path = pet_dir / "spritesheet.webp"
        preview_path = pet_dir / pet["preview"]
        for required_path in (manifest_path, atlas_path, preview_path):
            if not required_path.is_file():
                fail(f"{pet_id} is missing {required_path.relative_to(ROOT)}")

        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if set(manifest) != MANIFEST_FIELDS:
            fail(f"{pet_id} manifest must use only the supported Codex pet fields")
        if manifest["id"] != pet_id or manifest["displayName"] != pet["name"]:
            fail(f"{pet_id} catalog and manifest identities must match")
        if manifest["spriteVersionNumber"] != 2 or manifest["spritesheetPath"] != "spritesheet.webp":
            fail(f"{pet_id} must use the v2 spritesheet contract")

        destination = PREVIEW_ROOT / pet_id / "preview.gif"
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(preview_path, destination)
        public_pets.append(
            {
                **pet,
                "preview": f"assets/pets/{pet_id}/preview.gif",
                "repositoryUrl": f"https://github.com/designedbyomar/codex-pet-collective/tree/main/{pet['path']}",
            }
        )

    if featured != ["dj-bandit"]:
        fail("DJ Bandit must remain the sole featured launch pet")

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(json.dumps({"pets": public_pets}, indent=2) + "\n", encoding="utf-8")
    print(f"Built Pages catalog for {len(public_pets)} pets: {DATA_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

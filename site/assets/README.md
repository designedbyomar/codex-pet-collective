# Site assets

The fixed launch art stays here:

- `dj-bandit-hero.png` — editorial hero artwork
- `dj-bandit-social.png` — GitHub social-preview image
- `dj-bandit-preview.gif` — DJ Bandit motion preview
- `dj-bandit-atlas.png` — DJ Bandit's validated atlas overview

Pet-card imagery is release-owned rather than hand-managed here. Running
`python3 tools/build_site_catalog.py` validates [`pets/catalog.json`](../../pets/catalog.json)
and copies each approved `pets/<pet-id>/preview.gif` to
`site/assets/pets/<pet-id>/preview.gif` for Pages. Those generated copies are ignored by Git;
the source previews travel with their respective pet packages.

# Contributing to Codex Pet Collective

Thanks for helping give Codex more character.

## Submit a pet

1. Fork the repository and create a branch.
2. Copy `pets/TEMPLATE` to `pets/<pet-id>` using lowercase letters, numbers, and hyphens.
3. Add a valid `pet.json`, `spritesheet.webp`, `preview.gif`, and a short pet README with creator attribution.
4. Add one complete entry to `pets/catalog.json`, including species, actions, preview filename, and `featured: false`.
5. Run the v2 atlas validation and `python3 tools/build_site_catalog.py` before opening a pull request.
6. Include a screenshot or GIF in the pull request. The Pages roster is generated from the catalog, so no site-card edit is needed.

## Pet requirements

- Use Codex pet format v2: a transparent `1536 × 2288` atlas made of `192 × 208` cells.
- Use only the supported manifest fields: `id`, `displayName`, `description`, `spriteVersionNumber`, and `spritesheetPath`.
- Keep the pet readable at small sizes with no text, borders, scenery, or detached effects.
- Provide distinct, complete idle and activity animation frames.
- Do not submit content that infringes another creator’s rights, depicts a real person without permission, or uses a third-party logo/character.

## Attribution and license

Every contribution must name its creator in the pet README and be released under [CC BY 4.0](../LICENSE). You keep your copyright; the license lets the community share and adapt the work with attribution.

## Review

Maintainers check technical validity, visual coherence, animation readability, and attribution before merging. We may ask for targeted changes rather than restyling a pet without your approval.

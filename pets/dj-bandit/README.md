# DJ Bandit

The launch pet for Codex Pet Collective. DJ Bandit is a smooth, compact raccoon DJ who scratches records, dances between tasks, and glides backwards in a true moonwalk.

**Creator:** [Omar Tavarez / Designed by Omar](https://www.designedbyomar.com/)

**License:** [CC BY 4.0](../../LICENSE)

> Draft update: the livelier idle artwork is approved, but this branch is not release-ready. The full motion-quality gate found a pre-existing stationary jump row (0 px lift). Installation and merge are on hold pending a separately approved repair.

## Animation behavior

The updated idle has a gentle head nod, blink, and sway. Its preview uses the inspected desktop app's 6.6-second idle timing. The work-to-idle preview simulates three work cycles followed by idle; it is not a live app recording.

Continuous work playback is controlled by the app, not this manifest or atlas. In the inspected desktop version 26.1007.30912, the floating pet falls back to idle after approximately 2.46 seconds of work animation, and cursor-following can select a still pose. This artwork update does not fix that app behavior.

![Idle preview](idle-preview.gif)

## Install

Copy this entire folder to `~/.codex/pets/dj-bandit/`, then choose **DJ Bandit** in Codex pet settings.

## Contents

- `pet.json` — Codex v2 manifest
- `spritesheet.webp` — validated 8 × 11 animation atlas
- `preview.gif` — work-to-idle preview at inspected desktop timing
- `idle-preview.gif` — calm idle loop at inspected desktop timing
- `attribution.txt` — creator and licensing details


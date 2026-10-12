# DJ Bandit idle candidate — release hold

The user approved the revised idle artwork. Structural validation and full motion validation are separate checks.

| Check | Result |
| --- | --- |
| Encoded WebP | 1536 × 2288, 2,606,616 bytes |
| Required frames | 6, 8, 8, 4, 5, 8, 6, 6, 6, 8, 8 |
| Bundled atlas validator | Pass, no errors/warnings |
| Pets structural preflight | `valid: true` |
| Standard-frame inspection | Pass |
| Non-idle rows vs installed account baseline | All ten pixel-identical |
| Full motion-quality gate | **Fail: pre-existing jump row has 0 px airborne lift; minimum is 8 px** |

Candidate SHA-256: `9f291f129a4a5c06361e90b4a7fef41a7dd46ba7157ea6468a15ed1ee591e022`.

Idle holds are 1680, 660, 660, 840, 840, and 1920 ms (6600 ms total). Previews are rendered from the encoded candidate. Pointer overrides and status priority are not simulated in the GIF.

Compared with the installed account baseline, changes are limited to row 0: six new poses and clearing unused column 6. Compared with the older repository release, the candidate also includes the previously repaired work row and prior cleanup. The local installed package and account pet have not been replaced by this candidate.

Do not merge, deploy, or install this draft until the user approves expanding the idle-only scope to repair jump registration and the complete release checks pass. Do not waive the quality gate or silently modify the other approved animations.

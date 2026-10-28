# DJ Bandit idle and jump validation

The user approved the revised idle artwork and authorized the jump repair. Structural validation and full motion validation both pass.

| Check | Result |
| --- | --- |
| Encoded WebP | 1536 × 2288, 2,581,354 bytes |
| Required frames | 6, 8, 8, 4, 5, 8, 6, 6, 6, 8, 8 |
| Bundled atlas validator | Pass, no errors/warnings |
| Pets structural preflight | `valid: true` |
| Standard-frame inspection | Pass |
| Unaffected rows vs installed account baseline | All nine pixel-identical |
| Full motion-quality gate | Pass: 17 px airborne lift, 1 px landing delta |
| Stored account artwork | Decoded RGBA pixels match release exactly |
| Local package | SHA-256 matches release |

Release SHA-256: `27ca6ffaec8ab60ec9adc1578eac44c450c20ae9f8921bbf4b1eca86367d880a`.

Idle holds are 1680, 660, 660, 840, 840, and 1920 ms (6600 ms total). Previews are rendered from the encoded candidate. Pointer overrides and status priority are not simulated in the GIF.

Compared with the previous installed baseline, changes are limited to idle row 0 (including clearing unused column 6) and jump row 4. The approved idle pixels remain unchanged by the jump repair. Compared with the older repository release, this also includes the previously repaired work row and prior cleanup. The existing account pet and local package are updated, without a duplicate or metadata change.

Existing look-direction review warnings about subtle intermediate poses and source scale variation remain recorded in local QA; those rows were preserved. The full gate passed with reviewed warnings, not zero warnings across every check.

Continuous work looping still requires an app-side change. Live floating-pet playback has not been re-observed after installation. This pull request requires owner review before merge and Pages deployment.

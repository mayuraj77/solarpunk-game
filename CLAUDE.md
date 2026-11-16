# CLAUDE.md

Guidance for Claude working in this repository.

## What this is

An early prototype of an unnamed multiplayer solarpunk strategy game. Read `docs/design-summary.md` first. The living source of truth for decisions is the design log (link in that file); keep it updated when decisions change.

## The people

Two founders with no coding experience. Claude writes and maintains all code and picks the tools. Explain changes in plain language, without jargon. Prefer showing a playable result over describing one.

## Layout

| Path | What it is |
| --- | --- |
| `prototype/game.js` | All game logic and rendering (one IIFE, plain JavaScript, no dependencies) |
| `prototype/shell.html` | Page layout and styles |
| `prototype/solarpunk-valley.html` | Built single-file page. Generated: do not edit by hand |
| `art/aesthetic-directions.html` | Painted isometric mock-up and the four style directions |
| `docs/` | Design summary and the project hub page |
| `tools/build.py` | Builds the single-file page from shell + game |
| `tools/check.sh` | Syntax check plus one full headless session |
| `tools/sim/` | Balance simulations (see its README) |

## Workflow

After any change to `prototype/game.js` or `prototype/shell.html`:

1. `bash tools/check.sh` (must print "Syntax OK" and "ENDED after loop 11" with no runtime error).
2. `python3 tools/build.py`.
3. For balance changes, re-run the simulations in `tools/sim/` and compare with the targets in the design log.

There is no browser in the original development environment, so rendering is not tested automatically. Say so when reporting a change.

## Design rules to keep

- Decisions should come from planning, not clicking speed (APM must not decide results).
- No combat and no sabotage. Cooperation should pay in Standing.
- Energy comes only from sun, wind, water and muscle.
- The shared goal should succeed about 50% to 70% of the time in mixed lobbies.

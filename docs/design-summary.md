# Design summary

A snapshot of the design as of 16 November 2026. The full, living record is the **design log**: https://claude.ai/artifact/V2tSHj7XhE1Xf6DX6thEWJ. When they disagree, the design log wins.

## The game

An unnamed multiplayer game built on solarpunk as a concept: values first, not only the look. Players run settlements in a shared valley. They compete for **Standing** but share one goal, restoring the valley. If the shared goal fails, everyone fails ("competitive coexistence").

- **View:** isometric map with real elevation.
- **Art target:** hand-painted, Ghibli-like (references: *Dear Alice* by The Line, and the solarpunk art in Cole Hastings' "Solarpunk Is Gen Z's Future").
- **Aesthetic per setting:** mix and match directions (e.g. Earth & Pattern for a dry map, Clean Bright Utopia for another).
- **Platform:** cross-platform web game (browser on PC and phone), packaged later.
- **Team:** two people without coding experience; Claude writes the code.

## Core loop (prototype v0.4)

1. **Plan** (game paused): vote in the Valley Council, pick one research, place up to 3 buildings.
2. **Run** the season (30 ticks): production, weather, crises. Answer timed banners for crisis aid and trade offers.
3. **Settle:** people's food, water and energy needs are paid; meeting them grows your settlers; Skysail parts are delivered.
4. Repeat for 12 seasons, then rank by Standing.

## Key systems

| System | Summary |
| --- | --- |
| Four energies | Sun, wind, water and muscle only; output changes with season and weather |
| Settlers | Every building needs settlers to run it; gain settlers by meeting needs |
| The Doughnut (shared goal) | Needs met ≥ 75% on average, Valley Health ≥ 70, and the Skysail finished (30 parts) |
| Valley Council | One commons rule voted each season (Ostrom-style) |
| Crises and mutual aid | Droughts, storms, heatwaves; aid to a struck player counts triple |
| Restoration Credits | Earned only by healing the valley; spent on public works |
| Open knowledge | After anyone researches a technology, it costs everyone else 50% less |
| Specializations | Research spending builds persistent levels per branch, carried across sessions |
| Standing | 35% personal goal, 35% contribution to the shared goal, 15% development, 15% needs met |

## Proposed design pillars

1. Plan, don't race.
2. Better together, ranked apart.
3. Hope with stakes.
4. A world that remembers.

## Known issues (from ~1,700 simulated sessions)

- Green play (restore, rewild, give) takes the top rank too often (~58% of sessions).
- Needs are too easy to meet (~98%), so the floor never decides the outcome.
- Personal goals are uneven: Gardener is completed far less often than Feeder or Maker.
- "Everyone fails" lets one player sink the group; partial success tiers are proposed.

## Next steps

1. Fix rank dominance of green play and make needs matter; re-run simulations.
2. Human playtests with the success metrics in the design log.
3. Real multiplayer (2–8 players per session) with a hosted server.

## Links

- Project hub: https://claude.ai/artifact/RSmiswWVQDHHLNax1VJD2G
- Playable prototype: https://claude.ai/artifact/NRyh2sdGx7oYueEM6GNCWr
- Art direction: https://claude.ai/artifact/4QLCEjZXASaQig3Gm64MtQ

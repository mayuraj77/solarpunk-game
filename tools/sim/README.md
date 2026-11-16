# Balance simulations

Runs many automated sessions of the prototype with computer players only, to find dominant strategies and check how often the shared goal succeeds. Run everything from the repository root. Needs `uv`.

```bash
python3 tools/sim/patch.py                                   # make tools/sim/game_sim.js from prototype/game.js
uv run -q --no-project --with quickjs python -I tools/sim/run_sim.py baseline 100
uv run -q --no-project --with quickjs python -I tools/sim/run_sim.py uniform 40
python3 tools/sim/report.py                                  # summary of both runs
```

- `baseline N`: N sessions for each strategy in seat 1 (green, greedy, balanced, freerider), with the five other seats on their usual styles.
- `uniform N`: N sessions where all six seats use the same strategy.
- Results are written to `tools/sim/results/`.

`patch.py` edits a copy of the game so seat 1 is a computer player with a chosen style and adds a `__sim()` hook. If `prototype/game.js` changes the lines it looks for, `patch.py` stops with an assertion naming the missing text; update the matching line in `patch.py`.

Targets from the design log: shared goal success between 50% and 70% in mixed lobbies, and no single style taking the top rank far more often than its share of seats.

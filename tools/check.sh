#!/usr/bin/env bash
# Check the prototype without a browser. Run from the repository root:
#   bash tools/check.sh
# 1. Parses prototype/game.js to catch syntax errors.
# 2. Plays one full 12-season session headlessly with a fake page (tools/sim/harness.js)
#    and prints how it ended, to catch runtime errors.
# Needs `uv` (https://docs.astral.sh/uv/); it fetches the esprima and quickjs packages on demand.
set -euo pipefail
cd "$(dirname "$0")/.."

uv run -q --no-project --with esprima python -I -c "
import esprima
esprima.parseScript(open('prototype/game.js').read())
print('Syntax OK')"

cat tools/sim/harness.js prototype/game.js tools/sim/run.js > tools/sim/smoke_all.js
uv run -q --no-project --with quickjs python -I -c "
import quickjs
c = quickjs.Context(); out = []
c.add_callable('print', lambda s: out.append(str(s)))
try:
    c.eval(open('tools/sim/smoke_all.js').read())
except Exception as e:
    out.append('RUNTIME ERROR: ' + str(e))
print('\n'.join(o for o in out if o.startswith(('ENDED', 'RUNTIME', ' Session'))))"
rm -f tools/sim/smoke_all.js

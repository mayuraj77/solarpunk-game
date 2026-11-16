src=open('prototype/game.js').read()
def rep(a,b):
    global src
    assert a in src, a
    src=src.replace(a,b,1)
rep('R = rng(Date.now());','R = rng(globalThis.__seed || Date.now());')
rep('bot: i > 0,','bot: i > 0 || !!globalThis.__seed,')
rep('const BRANCH_ORDER = { green: ["living", "solar", "circular"], greedy: ["circular", "solar", "living"], balanced: ["solar", "circular", "living"] };',
    'const BRANCH_ORDER = { green: ["living", "solar", "circular"], greedy: ["circular", "solar", "living"], balanced: ["solar", "circular", "living"], freerider: ["circular", "solar", "living"] };')
rep('function botRun(p){','function botRun(p){\n  if (p.style === "freerider"){ if (p.credits >= 8) publicWork(p, "study"); ["timber", "crops", "ore", "fish", "water", "glass", "chips", "seeds"].forEach(k => { if (p.stock[k] < 5 && commons[k] >= 3) takeCommons(p, k, 5); }); return; }')
rep('newGame();\nrequestAnimationFrame(loop);','''globalThis.__sim = function(style0, others){
  STYLES[0] = style0; if (others) others.forEach((s, i) => STYLES[i + 1] = s);
  newGame(); started = true;
  let guard = 0;
  while (!ended && guard++ < 5000){ if (phase === "plan") beginSeason(); else step(); }
  const rows = players.map(p => ({ p, s: score(p) })).sort((a, b) => b.s.total - a.s.total);
  const txt = (document.querySelector("#dialog").innerHTML || "");
  return { ok: txt.indexOf("The valley is restored") >= 0, health: health, parts: parts, floor: valleyFloor(), tick: tick,
    ranking: rows.map(r => ({ style: r.p.style, id: r.p.id, score: Math.round(r.s.total), goal: r.p.goal, gp: r.s.gp, nd: r.s.nd, contrib: Math.round(r.p.contrib), techs: r.p.techs.size, settlers: r.p.settlers, buildings: r.p.buildings })),
    why: txt.replace(/<[^>]+>/g, " ").replace(/\\s+/g, " ").slice(0, 160) };
};
newGame();
requestAnimationFrame(loop);''')
open('tools/sim/game_sim.js','w').write(src)

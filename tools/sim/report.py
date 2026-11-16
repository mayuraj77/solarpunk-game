import json, collections, statistics as st
for mode in ['baseline','uniform']:
    res=json.load(open(f'tools/sim/results/{mode}.json'))
    print('=====',mode, len(res))
    by=collections.defaultdict(list)
    for r in res: by[r['p0']].append(r)
    for k,v in by.items():
        ok=sum(r['ok'] for r in v)/len(v); why=collections.Counter()
        for r in v:
            w=r['why']
            why['success' if r['ok'] else 'collapse' if 'collapsed' in w else 'skysail' if 'Skysail was not' in w else 'health' if 'Valley Health ended' in w else 'floor']+=1
        rank=[[x['id'] for x in r['ranking']].index(0)+1 for r in v]
        print(f"p0={k:9s} success={ok:.0%} health={st.mean(r['health'] for r in v):.1f} parts={st.mean(r['parts'] for r in v):.1f} floor={st.mean(r['floor'] for r in v):.2f} p0rank={st.mean(rank):.2f} {dict(why)}")
    if mode=='baseline':
        sc=collections.defaultdict(list); rk=collections.defaultdict(list)
        for r in res:
            for i,x in enumerate(r['ranking']): sc[x['style']].append(x['score']); rk[x['style']].append(i+1)
        for s in sc: print(f"  style {s:9s} avgScore={st.mean(sc[s]):.1f} avgRank={st.mean(rk[s]):.2f}")
        g=collections.defaultdict(list)
        for r in res:
            for x in r['ranking']: g[x['goal']].append(x['gp'])
        print('  goals:', {s: f"{st.mean(v):.0%}/{sum(1 for x in v if x>=1)/len(v):.0%}" for s,v in g.items()})
        top=collections.Counter(r['ranking'][0]['style'] for r in res); n=len(res)
        print('  top rank share', {k: f"{v/n:.0%}" for k,v in top.items()}, ' (green is 3/6 seats when p0 not green)')

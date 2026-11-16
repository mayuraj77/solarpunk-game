import quickjs, json, sys, time, collections
base = open('tools/sim/harness.js').read() + open('tools/sim/game_sim.js').read() + open('tools/sim/driver.js').read()
def run(expr):
    c = quickjs.Context(); c.add_callable('print', lambda s: None)
    c.eval(base); c.eval(expr)
    return json.loads(c.eval('JSON.stringify(__out)'))
mode = sys.argv[1]; n = int(sys.argv[2])
t=time.time()
if mode == 'baseline':
    res = run(f'runBatch(["green","greedy","balanced","freerider"], {n})')
elif mode == 'uniform':
    res = []
    for st in ["green","greedy","balanced","freerider"]:
        r = run(f'runBatch(["{st}"], {n}, ["{st}","{st}","{st}","{st}","{st}"])')
        res += r
json.dump(res, open(f'tools/sim/results/{mode}.json','w'))
print(mode, len(res), 'sessions in', round(time.time()-t,1), 's')

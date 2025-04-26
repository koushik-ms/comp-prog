from itertools import combinations

graph = {}

for edge_desc in open(0).readlines():
    s, d = edge_desc.strip().split("-")
    graph.setdefault(s, set()).add(d)
    graph.setdefault(d, set()).add(s)

comps = set()
cliques = set()

def clique(r, p, x):
    if not p and not x:
        # print(f"Clique detected: {r}")
        cliques.add(tuple(sorted(r)))
        for comb in combinations(r, 3):
            # print("Appending {}".format(comb))
            comps.add(tuple(sorted(comb)))
    while p:
        v = p.pop()
        clique(r | {v}, p & graph[v], x & graph[v])
        x.add(v)

nodes = set(graph.keys())
clique(set(), nodes, set())
ans = sum(1 if any(t.startswith('t') for t in comp) else 0 for comp in comps)
print("Part 1:", ans)

password = ",".join(max(cliques, key=len))
print("Part 2:", password)

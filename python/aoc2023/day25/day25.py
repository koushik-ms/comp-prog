from collections import defaultdict
from functools import reduce
from time import sleep
import networkx as nx
from .p01 import al

def partition_product(edgelist):
    G = nx.Graph()
    nodes = set()
    for er in edgelist:
        s, ts = er.split(":")
        s = s.strip()
        for t in ts.strip().split():
            G.add_edge(s, t, capacity=1.0)
            nodes.add(s)
            nodes.add(t)

    cut_edges = nx.minimum_edge_cut(G)
    G.remove_edges_from(cut_edges)
    p = list(nx.connected_components(G))
    return len(p[0]) * len(p[-1])
    # Choose one of the nodes that is not Dominant
    # cut_nodes = nx.minimum_node_cut(G)
    # nodes = [n for n in nodes if n not in cut_nodes]

    # Choose nodes that are not in the Dominant edges
    # cut_edges = nx.minimum_edge_cut(G)
    # nodes = [n for n in nodes if all(n not in e for e in cut_edges)]

    # Choose all nodes
    # nodes = list(nodes)
    # for j in range(1, len(nodes)):
    #     v, p = nx.minimum_cut(G, nodes[0], nodes[j])
    #     if v == 3:
    #         return len(p[0]) * len(p[-1])
    # v, p = nx.minimum_cut(G, nodes[0], nodes[-1])
    # return (v, p, nodes[0], nodes[-1])

def pg(el):
    print("Graph {")
    for e in el:
        s, r = e.split(": ")
        for t in r.strip().split():
            print(f"  {s} -- {t}")
    print("}")

def part1():
    print("AoC 2023: 25.1")
    tl = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr""".splitlines()
    # pg(al)
    pt = partition_product(tl)
    print(pt)
    assert pt == 54
    pa = partition_product(al)
    print(pa)
    assert pa == 583338


def part2():
    print("AoC 2023: 25.2")


if __name__ == "__main__":
    part1()
    part2()

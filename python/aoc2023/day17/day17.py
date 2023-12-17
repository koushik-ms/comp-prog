from .p01 import al
from heapq import heappush, heappop

DR = [1, 0, -1, 0]
DC = [0, -1, 0, 1]

def part1():
    print("AoC 2023: 17.1")
    ts = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".split("\n")
    pt = mp(ts)
    print(pt)
    assert pt == 102
    pa = mp(al)
    print(pa)
    assert pa == 970

def part2():
    print("AoC 2023: 17.2")
    ts = """111111111111
999999999991
999999999991
999999999991
999999999991""".split("\n")
    pt = up(ts)
    print(pt)
    assert pt == 71
    ts = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".split("\n")
    pt = up(ts)
    print(pt)
    assert pt == 94
    pa = up(al)
    print(pa)
    assert pa == 1149

def up(mat):
    G = [[int(c) for c in r] for r in mat]
    h = len(G)
    w = len(G[0]) if h else 0
    pp = []   # cost, row, col, direction, runlength
    heappush(pp, (0, 0, 0, 3, 0))
    heappush(pp, (0, 0, 0, 0, 0))
    seen = set()
    cost_profile = {}
    ans = -1
    while pp:
        cost, i, j, d, run = heappop(pp)
        if (i, j , d, run) in seen and cost >= cost_profile[(i, j, d, run)]:
            continue
        seen.add((i, j, d, run))
        cost_profile[(i, j, d, run)] = cost
        if i == (h-1) and j == (w-1):
            if run > 3 and (ans == -1 or ans > cost):
                ans = cost
            continue
        dl = []
        if run < 10:
            dl.append(d)
        if run > 3:
            dl.append((d+1)%4)
            dl.append((d+3)%4)
        for nd in dl:
            ni = i+DR[nd]
            nj = j+DC[nd]
            if 0<=ni<h and 0<=nj<w:
                nc = cost+G[ni][nj]
                nr = run+1 if d == nd else 1
                if (ni, nj, nd, nr) not in seen or nc < cost_profile[(ni, nj, nd, nr)]:
                    heappush(pp, (nc, ni, nj, nd, nr))
    return ans

def mp(mat):
    G = [[int(c) for c in r] for r in mat]
    h = len(G)
    w = len(G[0]) if h else 0
    pp = []   # cost, row, col, direction, runlength
    heappush(pp, (0, 0, 0, 3, 0))
    seen = set()
    cost_profile = {}
    ans = -1
    while pp:
        cost, i, j, d, run = heappop(pp)
        if (i, j , d) in seen:
            (pc, pr) = cost_profile[(i, j, d)]
            if cost >= pc and run >= pr:
                continue
        seen.add((i, j, d))
        cost_profile[(i, j, d)] = (cost, run)
        if i == (h-1) and j == (w-1):
            ans = cost if (ans == -1) else min(ans, cost)
            continue
        dl = [(d+1)%4, (d+3)%4]
        if run < 2:
            dl.append(d)
        for nd in dl:
            ni = i+DR[nd]
            nj = j+DC[nd]
            if 0<=ni<h and 0<=nj<w:
                if (ni, nj, nd) in seen:
                    pc, pr = cost_profile[(ni, nj, nd)]
                    if pc <= cost and pr <= run:
                        continue
                nr = (run+1) if d == nd else 0
                heappush(pp, (cost+G[ni][nj], ni, nj, nd, nr))
    return ans

if __name__ == "__main__":
    part1()
    part2()

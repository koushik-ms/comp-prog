from .p01 import al
from collections import deque

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
    print(mp(ts))
    print(mp(al))

def part2():
    print("AoC 2023: 17.2")
    ts = """111111111111
999999999991
999999999991
999999999991
999999999991""".split("\n")
    print(up(ts))
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
    print(up(ts))
    print(up(al))

def up(mat):
    G = [[int(c) for c in r] for r in mat]
    h = len(G)
    w = len(G[0]) if h else 0
    pp = deque()
    pp.append((0, 0, 3, 0, 0)) # , (0, 0, 3, 0, 0)
    pp.append((0, 0, 0, 0, 0)) # , (0, 0, 3, 0, 0)
    seen = set()
    sl = {}
    ans = -1
    while pp:
        i, j, d, cost, run = pp.popleft()
        if (i, j , d, run) in seen:
            pc = sl[(i, j, d, run)]
            if cost >= pc:
                continue
        seen.add((i, j, d, run))
        sl[(i, j, d, run)] = cost
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
                if (ni, nj, nd, nr) not in seen or nc < sl[(ni, nj, nd, nr)]:
                    pp.append((ni, nj, nd, nc, nr))
    return ans

def mp(mat):
    G = [[int(c) for c in r] for r in mat]
    h = len(G)
    w = len(G[0]) if h else 0
    pp = deque()
    pp.append((0, 0, 3, 0, 0))
    seen = set()
    sl = {}
    ans = -1
    while pp:
        i, j, d, cost, run = pp.popleft()
        if (i, j , d) in seen:
            (pc, pr) = sl[(i, j, d)]
            if cost >= pc and run >= pr:
                continue
        seen.add((i, j, d))
        sl[(i, j, d)] = (cost, run)
        if i == (h-1) and j == (w-1):
            ans = cost if (ans == -1) else min(ans, cost)
            continue
        for nd in [d, (d+1)%4, (d+3)%4]:
            ni = i+DR[nd]
            nj = j+DC[nd]
            if 0<=ni<h and 0<=nj<w:
                if (ni, nj, nd) in seen:
                    pc, pr = sl[(ni, nj, nd)]
                    if pc <= cost and pr <= run:
                        continue
                if d == nd:
                    if run < 2:
                        pp.append((ni, nj, nd, cost+G[ni][nj], run+1))
                else:
                    pp.append((ni, nj, nd, cost+G[ni][nj], 0))
    return ans

if __name__ == "__main__":
    part1()
    part2()

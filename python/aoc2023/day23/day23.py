import sys
from collections import defaultdict, deque
from time import sleep
from .p01 import al


DR = [1, 0, -1, 0]
DC = [0, 1, 0, -1]

eirs = {
    "." : list(range(4)),
    "v" : [0],
    ">" : [1],
    "^" : [2],
    "<" : [3],
}

firs = {
    "." : list(range(4)),
    "v" : list(range(4)),
    ">" : list(range(4)),
    "^" : list(range(4)),
    "<" : list(range(4)),
}

def lw(l, dirs = eirs, retpath=False):
    def longest_walk(already, sp, ep, seen):
        sr, sc = sp
        if sp == ep:
            return (already, seen)
        ch = mat[sr][sc]
        dl = dirs[ch]
        pl = []
        for d in dl:
            nr = sr + DR[d]
            nc = sc + DC[d]
            if 0<=nr<h and 0<=nc<w and mat[nr][nc] != "#" and f"({nr}, {nc})" not in seen:
                pl.append(longest_walk(already+1, (nr, nc), ep, seen + f"({sr}, {sc})"))
        ans = max(pl) if pl else (-1, seen)
        return ans

    mat = [[c for c in row] for row in l]
    h = len(mat)
    w = len(mat[0]) if h else 0
    sc = mat[0].index(".")
    sr = 0
    ec = mat[-1].index(".")
    er = h-1
    sc, path = longest_walk(0, (sr, sc), (er, ec), "")
    if retpath:
        return (sc, path)
    return sc

def lwt(l, dirs=firs):
    mat = [[c for c in row] for row in l]
    h = len(mat)
    w = len(mat[0]) if h else 0
    sr, sc = 0, mat[0].index(".")
    er, ec = h-1, mat[-1].index(".")
    BP = [(sr, sc)]
    bpc = 0
    for r in range(h):
        for c in range(w):
            if mat[r][c] == "#":
                continue
            brc = 0
            for d in dirs[mat[r][c]]:
                if 0<=(r+DR[d])<h and 0<=(c+DC[d])<w and mat[r+DR[d]][c+DC[d]] != "#":
                    brc += 1
            if brc > 2:
                bpc += 1
                BP.append((r, c))
    BP.append((er, ec))
    # print("Branching points count:", bpc)
    hallways = {}
    for rv, cv in BP:
        hallways[(rv,cv)] = []
        pp = deque([(rv, cv, 0)])
        seen = set()
        while pp:
            r, c, d = pp.popleft()
            if (r,c) in seen:
                continue
            seen.add((r,c))
            if (r,c) in BP and (r,c) != (rv, cv):
                hallways[(rv, cv)].append((r,c,d))
                continue
            for dr, dc in [(DR[d], DC[d]) for d in dirs[mat[r][c]]]:
                if 0<=(r+dr)<h and 0<=(c+dc)<w and mat[r+dr][c+dc] != "#":
                    pp.append((r+dr, c+dc, d+1))
        # print(f"{rv},{cv}: {hallways[(rv,cv)]}")
    # print("graph {")
    # for p in hallways:
    #     rr, rc = p
    #     for r, c, d in hallways[p]:
    #         print(f"    r{rr}c{rc} -- r{r}c{c} [label = {d}]")
    # print("}")
    visited = [[False for _ in range(w)] for _ in range(h)]
    state = {"ans": 0, "i":0 }
    def dfs(r, c, already):
        # state["i"] += 1
        # if state["i"]%10**6 == 0:
        #     print(state["i"])
        if visited[r][c]:
            return
        visited[r][c] = True
        if (r, c) == (er, ec):
            if already > state["ans"]:
                state["ans"] = already
                # print(state["ans"])
        for nr, nc, dd in hallways[(r,c)]:
            dfs(nr, nc, already + dd)
        visited[r][c] = False
    dfs(sr, sc, 0)
    print(f"Finally: {state['ans']=}")
    return state['ans']


def part1():
    print("AoC 2023: 23.1")
    tl = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#""".splitlines()
    sys.setrecursionlimit(3000)
    pt = lw(tl, dirs=eirs)
    print(pt)
    assert pt == 94
    pa = lw(al, dirs=eirs)
    print(pa)
    assert pa == 2110


def part2():
    print("AoC 2023: 23.2")
    tl = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#""".splitlines()
    sys.setrecursionlimit(9000)
    pt = lwt(tl, dirs = firs)
    print(pt)
    assert pt == 154
    pa = lwt(al, dirs=firs)
    print(pa)
    assert pa == 6514


if __name__ == "__main__":
    part1()
    part2()

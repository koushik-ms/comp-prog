from collections import defaultdict
from functools import reduce
from .p01 import al

DR = [1, 0, -1, 0]
DC = [0, -1, 0, 1]
HUGE = 1000000000

def dist(l, limit=64, wrap=False):
    mat = [[c for c in row] for row in l]
    # limit = 64
    r, c = 0, 0
    h = len(mat)
    w = len(mat[0]) if h else 0
    for i, row in enumerate(mat):
        if "S" in row:
            r = i
            c = row.index("S")
            break
    pp = [(r, c, int(0))]
    ans = 0
    mb = 0
    while pp:
        r, c, bl = pp.pop(0)
        if bl > mb:
            mb = bl
            # print(f"step {mb}")
        if bl == limit:
            ans += 1
        for d in range(4):
            nr = (r + DR[d])
            nc = (c + DC[d])
            if not wrap and 0<=nr<h and 0<=nc<w and mat[nr][nc] in ".S" and bl < limit and (nr,nc,bl+1) not in pp:
                pp.append((nr, nc, bl+1))
            if wrap and mat[nr%h][nc%w] in ".S" and bl < limit and (nr, nc, bl+1) not in pp:
                pp.append((nr, nc, bl+1))
    return ans

def part1():
    print("AoC 2023: 21.1")
    tl = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".split("\n")
    pt = dist(tl)
    print(pt)
    assert pt == 42
    pa = dist(al)
    print(pa)
    assert pa == 3746


def part2():
    print("AoC 2023: 21.2")
    tl = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".split("\n")
    # pt = dist(tl, limit=100, wrap=True)
    # print(pt)
    # assert pt == 42


if __name__ == "__main__":
    part1()
    part2()

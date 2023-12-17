from .p01 import al
from collections import deque

def part1():
    print("AoC 2023: 16.1")
    ts = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".split("\n")
    print(ce(ts))
    print(ce(al))

ddd = {
    ".": {
        ">": [(0, 1, ">")],
        "v": [(1, 0, "v")],
        "<": [(0, -1, "<")],
        "^": [(-1, 0, "^")],
    },
    "\\": {
        ">": [(1, 0, "v")],
        "v": [(0, 1, ">")],
        "<": [(-1, 0, "^")],
        "^": [(0, -1, "<")],
    },
    "/": {
        ">": [(-1, 0, "^")],
        "v": [(0, -1, "<")],
        "<": [(1, 0, "v")],
        "^": [(0, 1, ">")],
    },
    "|": {
        ">": [(-1, 0, "^"), (1, 0, "v")],
        "v": [(1, 0, "v")],
        "<": [(-1, 0, "^"), (1, 0, "v")],
        "^": [(-1, 0, "^")],
    },
    "-": {
        ">": [(0, 1, ">")],
        "v": [(0, 1, ">"), (0, -1, "<")],
        "<": [(0, -1, "<")],
        "^": [(0, 1, ">"), (0, -1, "<")],
    },
}

def ce(mat, start=(0,0, ">")):
    # print(mat)
    clo = [["?" for c in r] for r in mat]
    # print(clo)
    h = len(mat)
    w = len(mat[0]) if h else 0
    pp = deque()
    pp.append(start)
    while pp:
        i,j, d = pp.popleft()
        # print(f"AT: {i}, {j}, {d}")
        # clo[i][j] = "2" if (clo[i][j] != "?" and clo[i][j] != d) else d
        if clo[i][j] == "?":
            clo[i][j] = d
        elif clo[i][j] != d:
            clo[i][j] == "2"
        dm = ddd[mat[i][j]][d]
        for di, dj, dd in dm:
            if invalid(i+di, j+dj, h, w) or clo[i+di][j+dj] == "2" or clo[i+di][j+dj] == dd:
                continue
            pp.append((i+di, j+dj, dd))
        # print(f"({i}, {j}), => {pp}")
    # print("\n".join(str(r) for r in clo))
    ans = 0
    for i in range(h):
        for j in range(w):
            if clo[i][j] != "?":
                ans += 1
    return ans

def invalid(i, j, h, w):
    return not(0<=i<h and 0<=j<w)

def part2():
    print("AoC 2023: 16.2")
    ts = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".split("\n")
    print(all_pos(ts))
    print(all_pos(al))

def all_pos(mat):
    h = len(mat)
    w = len(mat[0]) if h else 0
    clo = [[0 for c in r] for r in mat]
    for i in [0, h-1]:
        if i == 0:
            d = "v"
        else:
            d = "^"
        for j in range(w):
            clo[i][j] = ce(mat, start=(i, j, d))
    for i in range(h):
        for j in [0, w-1]:
            if j == 0:
                d = ">"
            else:
                d = "<"
            clo[i][j] = max(clo[i][j], ce(mat, start=(i, j, d)))
    # print("\n".join(",".join(f"{c:03}" for c in r) for r in clo))
    return(max(max(r) for r in clo))

if __name__ == "__main__":
    part1()
    part2()


"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....



>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..
"""

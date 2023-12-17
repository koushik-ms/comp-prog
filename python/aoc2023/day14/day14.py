from .p01 import al
import pprint

def part1():
    print("AoC 2023: 14.1")
    tl = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".split("\n")
    print(load(tl))
    print(load(al))

def load(mat):
    G = [[c for c in row] for row in mat]
    h = len(mat)
    w = len(mat[0]) if h else 0
    ans = 0
    for j in range(w):
        oc = 0
        no = 0
        ca = 0
        for i in range(h):
            if G[i][j] == "#":
                oc = i+1
                no = 0
            if G[i][j] == "O":
                ca += h - (oc + no)
                no += 1
        # print(f"At {j}: {ans} + {ca} = {ca+ans}")
        ans += ca
    return ans

def part2():
    print("AoC 2023: 14.2")
    tl = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".split("\n")
    pt = cycle(tl, 1000)
    print(pt)
    assert pt == 69
    pa = cycle(al, 1000000000)
    print(pa)
    assert pa == 104815

def cycle(mat, spins):
    G = [[c for c in row] for row in mat]
    sh = {}
    s, i = -1, 0
    while i < spins:
        for op in [do_north, do_west, do_south, do_east]:
            op(G)
        s = ld(G)
        if s in sh:
            sh[s].append(i+1)
            if len(sh[s]) > 2:
                loclist = sh[s]
                if loclist[1]-loclist[0] == loclist[2] - loclist[1]:
                    d = loclist[1] - loclist[0]
                    i += d * ((spins - (i+1))//d)
        else:
            sh[s] = [i+1]
        i += 1
    return s

def ld(G):
    h = len(G)
    w = len(G[0]) if h else 0
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += h-i if G[i][j] == "O" else 0
    return ans


def do_north(G):
    h = len(G)
    w = len(G[0]) if h else 0
    for j in range(w):
        offset_row = 0
        no = 0
        for i in range(h):
            if G[i][j] == "#":
                offset_row = i+1
                no = 0
            if G[i][j] == "O":
                (G[offset_row+no][j], G[i][j]) = (G[i][j], G[offset_row+no][j])
                no += 1
        # print(f"At {j}:")
        # print('\n'.join(str(r) for r in G))

def do_west(G):
    h = len(G)
    w = len(G[0]) if h else 0
    for i in range(h):
        offset_col = 0
        no = 0
        for j in range(w):
            if G[i][j] == "#":
                offset_col = j+1
                no = 0
            if G[i][j] == "O":
                (G[i][offset_col+no], G[i][j]) = (G[i][j], G[i][offset_col+no])
                no += 1
        # print(f"At {j}:")
        # print('\n'.join(str(r) for r in G))

def do_south(G):
    h = len(G)
    w = len(G[0]) if h else 0
    for j in range(w):
        offset_row = h-1
        no = 0
        for i in range(h-1, -1, -1):
            if G[i][j] == "#":
                offset_row = i-1
                no = 0
            if G[i][j] == "O":
                (G[offset_row-no][j], G[i][j]) = (G[i][j], G[offset_row-no][j])
                no += 1
        # print(f"At {j}:")
        # print('\n'.join(str(r) for r in G))

def do_east(G):
    h = len(G)
    w = len(G[0]) if h else 0
    for i in range(h):
        offset_col = w-1
        no = 0
        for j in range(w-1, -1, -1):
            if G[i][j] == "#":
                offset_col = j-1
                no = 0
            if G[i][j] == "O":
                (G[i][offset_col-no], G[i][j]) = (G[i][j], G[i][offset_col-no])
                no += 1
        # print(f"At {j}:")
        # print('\n'.join(str(r) for r in G))

if __name__ == "__main__":
    part1()
    part2()

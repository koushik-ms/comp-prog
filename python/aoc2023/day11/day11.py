from .p01 import al

def process(mat, factor=2):
    h = len(mat)
    w = len(mat[0]) if h else 0
    row_has_g = ['.']*h
    col_has_g = ["."]*w
    gn = 0
    locs = []
    for y, row in enumerate(mat):
        for x, c in enumerate(row):
            if c == "#":
                row_has_g[y] = "#"
                col_has_g[x] = "#"
                locs.append({ "x": x, "y": y })
                gn += 1
    for g in locs:
        g["y"] += row_has_g[:g["y"]].count(".")*(factor-1)
        g["x"] += col_has_g[:g["x"]].count(".")*(factor-1)
    l = []
    for i in range(gn):
        for j in range(i+1, gn):
            l.append(manhat(locs[j], locs[i]))
    return sum(l)

def manhat(a, b):
    return abs(a["x"]-b["x"]) + abs(a["y"] - b["y"])


def part1():
    print("AoC 2023: 11.1")
    ts = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split("\n")
    print(process(ts))
    print(process(al))

def part2():
    print("AoC 2023: 11.2")
    ts = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split("\n")
    print(process(ts, factor=10))
    print(process(ts, factor=100))
    print(process(ts, factor=1000000))
    print(process(al, factor=1000000))


if __name__ == "__main__":
    part1()
    part2()

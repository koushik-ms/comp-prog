from .p01 import al

DR = [1, 0, -1, 0]
DC = [0, -1, 0, 1]
DM = {"D": 0, "L": 1, "U": 2, "R": 3}


def area(points, wl):
    enclosed_area = 0
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        enclosed_area += p1[0] * p2[1] - p2[0] * p1[1]
    return enclosed_area // 2 + wl // 2 + 1


def parse1(s):
    direction_code, sc, _ = s.split()
    return DM[direction_code], int(sc)


def parse2(s):
    cc = s.split()[-1].strip("(#) \t\n")
    sc = int(f"0x{cc[:-1]}", base=16)
    direction_code = (int(cc[-1]) + 3) % 4
    return direction_code, sc


def extent(l, parsing_function=parse1):
    i = 0
    j = 0
    contour: list[tuple[int, int]] = list([(i, j)])
    wall_length = 0
    for s in l:
        d, ns = parsing_function(s)
        i += DR[d] * ns
        j += DC[d] * ns
        contour.append((i, j))
        wall_length += ns
    return area(contour[::-1], wall_length)


def part1():
    print("AoC 2023: 18.1")
    ts = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".split(
        "\n"
    )
    pt = extent(ts)
    print(pt)
    assert pt == 62
    pa = extent(al)
    print(pa)
    assert pa == 45159


def part2():
    print("AoC 2023: 18.2")
    ts = "R 6 (#70c710)"
    assert parse1(ts) == (3, 6)
    assert parse2(ts) == (3, 461937)
    tl = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".split(
        "\n"
    )
    pt = extent(tl, parsing_function=parse2)
    print(pt)
    assert pt == 952408144115
    pa = extent(al, parsing_function=parse2)
    print(pa)
    assert pa == 134549294799713


if __name__ == "__main__":
    part1()
    part2()

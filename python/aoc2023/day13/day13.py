from .p01 import al

def part1():
    print("AoC 2023: 13.1")
    ts = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.""".split("\n")
    print(rr(ts), rc(ts))
    ts = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".split("\n")
    print(rr(ts), rc(ts))
    tl = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".split("\n\n")
    print(pr(tl))
    print(pr(al))

def rr(mat):
    l = len(mat)
    locs = []
    for i in range(1, l):
        if eq_row(mat, i, i-1):
            locs.append(i)
    res = []
    for loc in locs:
        is_ref = True
        for i in range(loc):
            if loc+i>=l or (loc-1-i)<0:
                if is_ref:
                    res.append(loc)
                break
            if not eq_row(mat, loc+i, loc-1-i):
                is_ref = False
        if is_ref:
            res.append(loc)
    return max(res) if res else 0

def rc(mat):
    l = len(mat[0]) if mat else 0
    locs = []
    for i in range(1, l):
        if eq_col(mat, i, i-1):
            locs.append(i)
    res = []
    for loc in locs:
        is_ref = True
        for i in range(loc):
            if loc+i>=l or (loc-1-i)<0:
                if is_ref:
                    res.append(loc)
                break
            if not eq_col(mat, loc+i, loc-1-i):
                is_ref = False
        if is_ref:
            res.append(loc)
    return max(res) if res else 0

def eq_row(mat, i, j):
    return mat[i]  == mat[j]

def eq_col(mat, i, j):
    return all([row[i] == row[j] for row in mat])

def pr(mats, rcf = rr, ccf = rc):
    mats = [mat.split("\n") for mat in mats]
    sr, sc = 0, 0
    for mat in mats:
        r, c = rcf(mat), ccf(mat)
        # print(f"{sr}, {sc} + {r}, {c} => ", end="")
        sr += r
        sc += c
        # print(f"{sr}, {sc}")
    return 100*sr + sc

def part2():
    print("AoC 2023: 13.2")
    ts = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.""".split("\n")
    print(rr_flip(ts), rc_flip(ts))
    ts = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".split("\n")
    print(rr_flip(ts), rc_flip(ts))
    tl = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".split("\n\n")
    print(pr(tl, rcf=rr_flip, ccf=rc_flip))
    print(pr(al, rcf=rr_flip, ccf=rc_flip))

def rr_flip(mat):
    h = len(mat)
    w = len(mat[0]) if mat else 0
    for i in range(h-1):
        flippable = 0
        # print(f" {i}: ", end="")
        for d in range(h):
            t = i-d
            b = i+1+d
            if 0<=t<b<h:
                for k in range(w):
                    if mat[t][k] != mat[b][k]:
                        # print(f"bat({d}) {t},{k}, ", end="")
                        flippable += 1
        if flippable == 1:
            # print(" =>> FLIPPABLE")
            return i+1
        # print()
    return 0

def rc_flip(mat):
    h = len(mat)
    w = len(mat[0]) if mat else 0
    for j in range(w-1):
        flippable = 0
        # print(f" {j}: ", end="")
        for d in range(w):
            l = j-d
            r = j+1+d
            if 0<=l<r<w:
                for k in range(h):
                    if mat[k][l] != mat[k][r]:
                        # print(f"bat({d}) {l},{k}, ", end="")
                        flippable += 1
        if flippable == 1:
            # print(" =>> FLIPPABLE")
            return j+1
        # print()
    return 0

if __name__ == "__main__":
    part1()
    part2()

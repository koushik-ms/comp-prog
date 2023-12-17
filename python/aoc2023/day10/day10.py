from .p01 import al

def part1():
    print("AoC 2023: 10.1")
    ts = """.....
.S-7.
.|.|.
.L-J.
.....""".split("\n")
    ts = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ""".split("\n")
    print(gsc(ts))
    print(ll(ts)/2)
    print(ll(al)/2)

def part2():
    print("AoC 2023: 10.2")
    ts = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........""".split("\n")
    print(cs(ts))
    ts = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...""".split("\n")
    print(cs(ts))
    ts = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""".split("\n")
    print(cs(ts))
    print(cs(al))

def cs(mat):
    ans = 0
    clo = ["O"*len(mat[0]) for _ in mat]
    print(clo)
    ns = ll(mat, clo)
    print(clo)
    for i,x in enumerate(clo):
        io = 0
        on = False
        bb = ""
        for j,c in enumerate(x):
            if c in "B":
                if mat[i][j] in "|":
                    # print(f"Switching at {i},{j}")
                    io += 1
                if mat[i][j] in "LF":
                    on = True
                    bb = mat[i][j]
                if mat[i][j] in "7SJ":
                    on = False
                    if (bb == "L" and mat[i][j] in "7S") or (bb == "F" and mat[i][j] == "J"):
                        io += 1
                        # print(f"Switching at {i},{j}")
                    bb = ""
                # print(f"B at ({i},{j}): io = {io}")
            else:
                ans += io%2
                print(f"{i},{j} {io%2} => {ans}")
    return ans

def ll(l, clo=None):
    sp = gsc(l)
    cp = fnp(sp, l)
    ns = 1
    while cp:
        np = fnp(cp[0], l, sp)
        if clo:
            clo[sp[0]] = clo[sp[0]][:sp[1]] + "B" + clo[sp[0]][sp[1]+1:]
        sp = cp[0]
        cp = np
        ns = ns +1
    if clo:
        clo[sp[0]] = clo[sp[0]][:sp[1]] + "B" + clo[sp[0]][sp[1]+1:]
    return ns

def fnp(p, mat, pp = None):
    i, j = p
    h, w = len(mat), len(mat[0])
    res = []
    start = (mat[i][j] == "S")
    if i>0 and mat[i-1][j] in "|7F" and pp != ((i-1, j)) and (start or mat[i][j] in "|JL"):
        res.append((i-1, j))
    if j>0 and mat[i][j-1] in "-FL" and pp != ((i, j-1)) and (start or mat[i][j] in "-J7"):
        res.append((i, j-1))
    if i<(h-1) and mat[i+1][j] in "|JL" and pp != ((i+1, j)) and (start or mat[i][j] in "|7F"):
        res.append((i+1, j))
    if j<(w-1) and mat[i][j+1] in "-7J" and pp != ((i, j+1)) and (start or mat[i][j] in "-FL"):
        res.append((i, j+1))
    return res

def gsc(l):
    for i, s in enumerate(l):
        if "S" in s:
            return i, s.find("S")
    return 0,0

if __name__ == "__main__":
    part2()

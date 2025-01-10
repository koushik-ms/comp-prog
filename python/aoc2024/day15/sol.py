gpm = open(0).read()
grid, moves = gpm.split("\n\n")

grid = [list(r.strip()) for r in grid.splitlines()]
og = [list(r) for r in grid]
dd = {
    "<": [0, -1],
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
}
moves = "".join(s.strip() for s in moves.splitlines())


def find_starting_position(mat, sc="@"):
    for r, col in enumerate(mat):
        for c, v in enumerate(col):
            if v == sc:
                return r, c
    return 0, 0


def find_swap_point(mat, sr, sc, dir):
    dr, dc = dd[dir]
    cr, cc = sr, sc
    while True:
        if mat[cr][cc] == ".":
            return cr, cc
        if mat[cr][cc] == "#":
            break
        cr += dr
        cc += dc
    return -1, -1


rows = len(grid)
cols = len(grid[0])
sr, sc = find_starting_position(grid)


def part1():
    global rows, cols, sr, sc
    for md in moves.strip():
        tr, tc = find_swap_point(grid, sr, sc, md)
        if tr < 0 or tc < 0:
            continue
        dot = grid[tr][tc]
        dr, dc = dd[md]
        if dr != 0:
            for r in range(tr, sr, -1 * dr):
                grid[r][sc] = grid[r - dr][sc]
            grid[sr][sc] = dot
        else:
            for c in range(tc, sc, -1 * dc):
                grid[sr][c] = grid[sr][c - dc]
            grid[sr][sc] = dot

        sr += dr
        sc += dc
        # print("\n".join("".join(r) for r in grid))


part1()
ans = sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "O")
print("Part 1: ", ans)

# double the grid
wt = {
    "O": "[]",
    ".": "..",
    "#": "##",
    "@": "@.",
}
wgrid = [[wt[og[r][c]] for c in range(cols)] for r in range(rows)]
wgrid = [list("".join(wgrid[r][c] for c in range(cols))) for r in range(rows)]
rows = len(wgrid)
cols = len(wgrid[0])
sr, sc = find_starting_position(wgrid)
# for r in wgrid:
#     print(*r, sep="")
# print(f"Starting at {(sr, sc)}")
cr, cc = sr, sc
for m in moves.strip():
    dr, dc = dd[m]
    o2m = [(cr, cc)]
    seen = set()
    blocked = False
    for r, c in o2m:
        if (r, c) in seen:
            continue
        seen.add((r, c))
        r += dr
        c += dc
        if wgrid[r][c] == "#":
            blocked = True
            break
        elif wgrid[r][c] == "]":
            o2m.append((r, c))
            o2m.append((r, c - 1))
        elif wgrid[r][c] == "[":
            o2m.append((r, c))
            o2m.append((r, c + 1))
    if blocked:
        continue
    wgc = [list(r) for r in wgrid]
    # wgrid[cr][cc] = "."
    for r, c in o2m:
        wgrid[r][c] = "."
    for r, c in o2m[1:]:
        wgrid[r + dr][c + dc] = wgc[r][c]
    cr += dr
    cc += dc
    wgrid[cr][cc] = "@"

ans = sum(100 * r + c for r in range(rows) for c in range(cols) if wgrid[r][c] == "[")
print("Part 2:", ans)

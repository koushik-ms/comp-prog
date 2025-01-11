grid = [list(map(int, r.strip())) for r in open(0).readlines()]
# for r in grid:
#     print(*r, sep="")
# print(grid)


def trails_from(sr, sc, grid) -> set[tuple[int, int]]:
    c = grid[sr][sc]
    rows = len(grid)
    cols = len(grid[0])  # How much does optimizing this save ?

    if c == 9:
        return {(sr, sc)}

    def inb(r, c):
        return (0 <= r < rows) and (0 <= c < cols)

    ans = set()
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        cr = sr + dr
        cc = sc + dc
        if inb(cr, cc) and grid[cr][cc] == c + 1:
            ans.update(trails_from(cr, cc, grid))
    return ans


def distinct_trails_from(sr, sc, grid) -> set[str]:
    c = grid[sr][sc]
    rows = len(grid)
    cols = len(grid[0])  # How much does optimizing this save ?

    if c == 9:
        return {"({},{})".format(sr, sc)}

    def inb(r, c):
        return (0 <= r < rows) and (0 <= c < cols)

    ans = set()
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        cr = sr + dr
        cc = sc + dc
        if inb(cr, cc) and grid[cr][cc] == c + 1:
            for trail in distinct_trails_from(cr, cc, grid):
                ans.add("({}, {})->{}".format(sr, sc, trail))
    return ans


rows = len(grid)
cols = len(grid[0])

ans = sum(
    len(trails_from(r, c, grid))
    for r in range(rows)
    for c in range(cols)
    if grid[r][c] == 0
)
print(ans)

ans = sum(
    len(distinct_trails_from(r, c, grid))
    for r in range(rows)
    for c in range(cols)
    if grid[r][c] == 0
)
print(ans)

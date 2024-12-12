#!/usr/bin/env python

grid = [list(s.strip()) for s in open(0).readlines()]
# print(grid)

h = len(grid)
w = len(grid[0])
area = {}
peri = {}
seen = [[False] * w for _ in range(h)]

inb = lambda r, c: (0 <= r < h) and (0 <= c < w)
oob = lambda r, c: not inb(r, c)

area = 0
perimeter = 0
ans = 0
regions: list[set[tuple[int, int]]] = []
for r, row in enumerate(grid):
    for c, plant in enumerate(row):
        # print(f"Plant {plant}")
        if seen[r][c]:
            continue
        seen[r][c] = True
        region = {(r, c)}
        qq = {(r, c)}
        while qq:
            cr, cc = qq.pop()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = cr + dr
                nc = cc + dc
                if oob(nr, nc):
                    continue
                if grid[nr][nc] != plant:
                    continue
                if (nr, nc) in region:
                    continue
                qq.add((nr, nc))
                region.add((nr, nc))
                seen[nr][nc] = True
        regions.append(region)


def get_perimeter(region: set[tuple[int, int]]):
    ans = 0
    for r, c in region:
        ans += 4
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr, nc) in region:
                ans -= 1
    return ans


ans = sum(len(r) * get_perimeter(r) for r in regions)
print(f"Ans: {ans}")


def get_num_sides(region: set[tuple[int, int]]):
    ans = 0
    side2gap: dict[tuple[float, float], tuple[float, float]] = {}
    for r, c in region:
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr, nc) in region:
                continue
            sr = (r + nr) / 2
            sc = (c + nc) / 2
            side2gap[(sr, sc)] = (r - sr, c - sc)
    visited: set[tuple[float, float]] = set()
    for side, gaps in side2gap.items():
        if side in visited:
            continue
        visited.add(side)
        sr, sc = side
        if int(sr) == sr:
            for direction in [1, -1]:
                nr = sr + direction
                while (nr, sc) in side2gap and side2gap[(nr, sc)] == gaps:
                    visited.add((nr, sc))
                    nr += direction
        else:
            for direction in [1, -1]:
                nc = sc + direction
                while (sr, nc) in side2gap and side2gap[(sr, nc)] == gaps:
                    visited.add((sr, nc))
                    nc += direction
        ans += 1
    return ans


ans = sum(len(r) * get_num_sides(r) for r in regions)
print(f"Ans: {ans}")

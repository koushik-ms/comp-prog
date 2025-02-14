from collections import deque


points = [list(map(int, x.split(","))) for x in open(0).readlines()]

rows = cols = 71
step_limit = 1024
grid = [["."] * cols for _ in range(rows)]

i = 0
while i < step_limit:
    c, r = points[i]
    grid[r][c] = "#"
    i += 1


def path_cost(grid) -> int:
    sr, sc = 0, 0
    er, ec = rows - 1, cols - 1
    seen = set()
    q = deque([(0, sr, sc)])
    while q:
        cost, cr, cc = q.popleft()
        if (cr, cc) in seen:
            continue
        seen.add((cr, cc))
        if cr == er and cc == ec:
            return cost
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            r = cr + dr
            c = cc + dc
            if (0 <= r < rows) and (0 <= c < cols) and grid[r][c] != "#":
                q.append((cost + 1, r, c))
    return -1


print(f"Part 1: { path_cost(grid) }")

while i < len(points):
    c, r = points[i]
    grid[r][c] = "#"

    cost = path_cost(grid)
    if cost < 0:
        print("Part 2: {}".format(points[i]))
        break
    i += 1

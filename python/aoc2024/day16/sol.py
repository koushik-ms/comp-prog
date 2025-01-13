from collections import deque

dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_first_from_topleft(mat, t="S") -> tuple[int, int]:
    for r, row in enumerate(mat):
        for c, val in enumerate(row):
            if val == t:
                return (r, c)
    return (-1, -1)


def get_path_costs(grid):
    er, ec = find_first_from_topleft(grid, "E")

    rows = len(grid)
    cols = len(grid[0])
    dp = [float("inf")] * 4
    path_costs = [[list(dp) for _ in range(cols)] for _ in range(rows)]
    path_costs[er][ec] = [0.0] * 4

    ss = deque([(er, ec)])
    while ss:
        cr, cc = ss.popleft()
        for neighbour_dir in range(4):
            dr, dc = dd[neighbour_dir]
            move_dir = (neighbour_dir + 2) % 4
            if grid[cr + dr][cc + dc] == "#":
                continue
            mc = min(
                path_costs[cr][cc][move_dir] + 1,
                path_costs[cr][cc][(move_dir + 1) % 4] + 1001,
                path_costs[cr][cc][(move_dir + 3) % 4] + 1001,
            )
            if mc < path_costs[cr + dr][cc + dc][move_dir]:
                ss.append((cr + dr, cc + dc))
                path_costs[cr + dr][cc + dc][move_dir] = mc

    return path_costs


def solve1(path_costs, sp):
    sr, sc = sp
    # We start facing east. So northerly/ southerly paths incur extra starting
    # cost to turn
    ans, ans_dir = min(
        (path_costs[sr][sc][0], 0),
        (path_costs[sr][sc][1] + 1000, 1),
        (path_costs[sr][sc][3] + 1000, 3),
    )
    return int(ans), ans_dir


def solve2(grid, path_costs, sp, sd):
    rows = len(grid)
    cols = len(grid[0])
    sr, sc = sp
    dr, dc = dd[int(sd)]
    ss = deque([(sr + dr, sc + dc, path_costs[sr][sc][sd], sd)])
    while ss:
        cr, cc, cost, cd = ss.popleft()
        if grid[cr][cc] == ".":
            grid[cr][cc] = "O"
        for delta in [-1, 0, 1]:
            dindex = (cd + delta) % 4
            cost_limit = (cost - 1) if delta == 0 else (cost - 1001)
            dr, dc = dd[dindex]
            if path_costs[cr][cc][dindex] <= cost_limit:
                ss.append((cr + dr, cc + dc, cost_limit, dindex))
    return sum(1 for r in range(rows) for c in range(cols) if grid[r][c] in "OSE")


def solve(grid):
    path_costs = get_path_costs(grid)
    (sr, sc) = find_first_from_topleft(grid)
    ans, ans_dir = solve1(path_costs, (sr, sc))
    ans2 = solve2(grid, path_costs, (sr, sc), ans_dir)
    return ans, ans2


def main():
    grid = [list(r.strip()) for r in open(0).readlines()]
    path_costs = get_path_costs(grid)
    (sr, sc) = find_first_from_topleft(grid)
    ans, ans_dir = solve1(path_costs, (sr, sc))
    print("Ans: ", ans, "dir: ", ans_dir)
    print("Ans:", solve2(grid, path_costs, (sr, sc), ans_dir))


if __name__ == "__main__":
    main()

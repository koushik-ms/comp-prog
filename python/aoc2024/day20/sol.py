grid = [list(s.strip()) for s in open(0).readlines()]

H = len(grid)
W = len(grid[0])


def get_start_location(mat, rows, cols, start_char="S"):
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == start_char:
                return (i, j)
    return -1, -1


def get_path_lengths(grid):
    q: list[tuple[int, int, int]] = [(0, er, ec)]
    seen = set()
    pl = None
    path_lengths = {}

    while q:
        cost, r, c = q.pop()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if grid[r][c] == "S" and pl is None:
            pl = cost
        if pl is not None and pl < cost:
            continue
        path_lengths[(r, c)] = min(cost, path_lengths.get((r, c), H * W * 2))
        for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            nr = r + dr
            nc = c + dc
            if grid[nr][nc] == "#":
                continue
            q.append((cost + 1, nr, nc))
    return path_lengths


def valid_cheat(dc, dist, part1):
    if part1:
        return dist == 2 and dc > 2
    return dist <= 20 and dc > dist


def get_cheats(path_lengths, part1=True):
    cheats: dict[int, int] = {}
    for r, c in path_lengths.keys():
        for tr, tc in path_lengths.keys():
            if (tr, tc) > (r, c):
                continue
            dist = abs(tr - r) + abs(tc - c)
            dc = abs(path_lengths[(r, c)] - path_lengths[(tr, tc)])
            if valid_cheat(dc, dist, part1):
                if dc - dist not in cheats.keys():
                    cheats[dc - dist] = 0
                cheats[dc - dist] += 1
    return cheats


er, ec = get_start_location(grid, H, W, start_char="E")
path_lengths = get_path_lengths(grid)
for part in range(2):
    cheats = get_cheats(path_lengths, part == 0)
    ans = sum(v for k, v in cheats.items() if k >= 100)
    print(f"Part{1+part}\nAns: {ans}\n")


# Fancy cheat table printing
# for c in sorted(cheats.keys()):
#     v = cheats[c]
#     # print(
#     #     "There {} {} {} that {} {} picoseconds".format(
#     #         "are" if v > 1 else "is",
#     #         v if v > 1 else "one",
#     #         "cheats" if v > 1 else "cheat",
#     #         "save" if v > 1 else "saves",
#     #         c,
#     #     )
#     # )
#     if c >= 100:
#         ans += v

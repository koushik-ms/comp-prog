from functools import cache

lock_kp_coords = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "gap": (0, 3),
    "0": (1, 3),
    "A": (2, 3),
}

dir_kp_coords = {
    "gap": (0, 0),
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}

dir = {"^": [0, -1], ">": [1, 0], "v": [0, 1], "<": [-1, 0]}


@cache
def codes2jump(adj_pos, level=2):
    cx, cy = dir_kp_coords[adj_pos[0]]
    tx, ty = dir_kp_coords[adj_pos[1]]
    path = [move + "A" for move in revise_path(cx, cy, tx, ty, dir_kp_coords["gap"])]
    mcl = min(len(s) for s in path)
    path = [s for s in path if len(s) == mcl]
    if level == 1:
        return min(len(s) for s in path)
    return min(
        sum(codes2jump(c + d, level - 1) for c, d in zip("A" + code, code))
        for code in path
    )


@cache
def path_coords(start_pos, path):
    res = [start_pos]
    cx, cy = start_pos
    for code in path:
        dx, dy = dir[code]
        cx += dx
        cy += dy
        res.append((cx, cy))
    return res


@cache
def revise_path(cx, cy, tx, ty, gap_coords):
    dx, dy = (tx - cx), (ty - cy)
    sx = ">" * dx if dx > 0 else "<" * abs(dx)
    sy = "v" * dy if dy > 0 else "^" * abs(dy)
    combis = [sx + sy]
    if dx != 0 and dy != 0:
        combis.append(sy + sx)
    combis = [path for path in combis if gap_coords not in path_coords((cx, cy), path)]
    if len(combis) < 1:
        print(f"Empty list for {(cx, cy)} -> {(tx, ty)}")
    return combis


def get_moves(code, co_ords, start_pos=None):
    res = [""]
    cx, cy = start_pos if start_pos is not None else co_ords["A"]
    for c in code:
        tx, ty = co_ords[c]
        combis = revise_path(cx, cy, tx, ty, co_ords["gap"])
        res = [pre + new + "A" for pre in res for new in combis]
        cx, cy = tx, ty
    return res


def get_complexity(kpc, num_robots=2):
    lock_robot_codes = get_moves(kpc, lock_kp_coords)
    code_length = min(
        sum(codes2jump(c + d, level=num_robots) for c, d in zip("A" + move, move))
        for move in lock_robot_codes
    )
    return code_length * int(kpc[:-1])


def solve(codes):
    ans = [
        sum(get_complexity(code, num_robots) for code in codes)
        for num_robots in [2, 25]
    ]
    return ans


if __name__ == "__main__":
    codes = [s.strip() for s in open(0).readlines()]
    for part, num_robots in [(1, 2), (2, 25)]:
        ans = sum(get_complexity(code, num_robots=num_robots) for code in codes)
        print(f"\nPart{part}\nAns: {ans}")

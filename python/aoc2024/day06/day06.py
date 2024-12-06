from tqdm import tqdm
from .p01 import al

offsets = {
    "^": (-1, 0, ">"),
    ">": (0, 1, "v"),
    "v": (1, 0, "<"),
    "<": (0, -1, "^"),
}


def part1():
    print("AoC 2024: 6.1")
    tl = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split(
        "\n"
    )
    ans = path_length([list(s) for s in tl])
    assert ans == 41, f"Expected: 41 vs {ans}"
    ans = path_length([list(s) for s in al])
    print("Part 1:", ans)
    assert ans == 4656, f"Expected: 4656 vs {ans}"


def path_length(mat: list[list[str]]) -> int:
    h = len(mat)
    w = len(mat[0])
    curpos = find_curpos(mat, w, h)
    pp = path(mat, curpos)
    return len(pp)


def oob(i: int, j: int, w: int, h: int) -> bool:
    return not ((0 <= i < w) and (0 <= j < h))


def find_curpos(mat: list[list[str]], w: int, h: int) -> tuple[int, int]:
    for r in range(h):
        for c in range(w):
            if mat[r][c] in "^>v<":
                return (r, c)
    return (-1, -1)


def path(mat: list[list[str]], start_pos: tuple[int, int]) -> set[tuple[int, int]]:
    curpos = start_pos
    h = len(mat)
    w = len(mat[0])
    pp: set[tuple[int, int]] = set()
    loop_detect: set[tuple[int, int, str]] = set()
    rd: str = "^"
    while not oob(*curpos, w, h):
        pp.add(curpos)
        r, c = curpos
        if (r, c, rd) in loop_detect:
            return set()
        loop_detect.add((r, c, rd))
        dr, dc, nd = offsets[rd]
        while not oob(r + dr, c + dc, w, h):
            if mat[r + dr][c + dc] == "#":
                rd = nd
                dr, dc, nd = offsets[rd]
            else:
                break
        curpos = (r + dr, c + dc)
    return pp


def loopy_obstacle_points(mat: list[list[str]]) -> int:
    h = len(mat)
    w = len(mat[0])
    curpos = find_curpos(mat, w, h)
    ans = 0
    original_path = path(mat, curpos)
    for r, c in tqdm(original_path):
        mat[curpos[0]][curpos[1]] = "^"
        if mat[r][c] != ".":
            continue
        mat[r][c] = "#"
        pl = path(mat, curpos)
        if len(pl) == 0:
            ans += 1
        mat[r][c] = "."
    return ans


def part2():
    print("AoC 2024: 6.2")
    tl = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split(
        "\n"
    )
    ans = loopy_obstacle_points([list(s) for s in tl])
    assert ans == 6, f"Expected: 6 vs {ans}"
    ans = loopy_obstacle_points([list(s) for s in al])
    print("\rPart 2:", ans)
    assert ans == 1575, f"Expected: 1575 vs {ans}"


if __name__ == "__main__":
    part1()
    part2()

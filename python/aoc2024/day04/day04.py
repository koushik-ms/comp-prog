from collections.abc import Sequence
from typing import LiteralString
from .p01 import al


def part1():
    print("AoC 2024: 4.1")
    tl = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split(
        "\n"
    )
    ans = word_search1(al)
    print("Part 1:", ans)
    assert ans == 2536, f"Expected: 2536 vs {ans}"


def word_search1(mat: Sequence[str | LiteralString]) -> int:
    h = len(mat)
    w = len(mat[0])
    # print(f"{w} x {h}")
    ans = 0
    for j in range(h):
        for i in range(w):
            for direction in "newsabcd":
                ans += find_xmas(direction, i, j, w, h, mat)
    return ans


offsets = {
    "n": [0, -1],
    "e": [1, 0],
    "w": [-1, 0],
    "s": [0, 1],
    "a": [1, 1],
    "b": [1, -1],
    "c": [-1, -1],
    "d": [-1, 1],
}


def find_xmas(
    sd: str | LiteralString,
    i: int,
    j: int,
    w: int,
    h: int,
    mat: Sequence[str | LiteralString],
    target_word: str | LiteralString = "XMAS",
) -> int:
    [ox, oy] = offsets[sd]
    # print(f"Search {i} {j} with offsets {ox}, {oy}")
    for tc in target_word:
        if oob(i, j, w, h):
            return 0
        if mat[j][i] != tc:
            return 0
        i += ox
        j += oy
    return 1


def oob(i: int, j: int, w: int, h: int) -> bool:
    return (i < 0) or (j < 0) or (i >= w) or (j >= h)


def find_mas(
    sd: str, i: int, j: int, w: int, h: int, mat: Sequence[str | LiteralString]
) -> int:
    [ox, oy] = offsets[sd]
    p1 = [i + ox, j + oy]
    p2 = [i - ox, j - oy]
    if oob(p1[0], p1[1], w, h) or oob(p2[0], p2[1], w, h):
        return 0
    c1 = mat[p1[1]][p1[0]]
    c2 = mat[p2[1]][p2[0]]
    oc = f"{c1}{c2}"
    if oc == "SM" or oc == "MS":
        return 1
    return 0


def word_search2(mat: Sequence[str | LiteralString]) -> int:
    h = len(mat)
    w = len(mat[0])
    # print(f"{w} x {h}")
    ans = 0
    for j in range(h):
        for i in range(w):
            if mat[j][i] == "A":
                dm = sum(find_mas(sd, i, j, w, h, mat) for sd in "ad")
                if dm == 2:
                    # print(f"Found X-MAS at {i}, {j}")
                    ans += 1
    return ans


def part2():
    print("AoC 2024: 4.2")
    tl = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split(
        "\n"
    )
    ans = word_search2(al)
    print("Part 2:", ans)
    assert ans == 1875, f"Expected: 1875 vs {ans}"


if __name__ == "__main__":
    part1()
    part2()

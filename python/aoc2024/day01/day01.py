from collections.abc import Sequence
from typing import LiteralString
from .p01 import al


def get_locations_lists(
    spaced_entries: Sequence[str | LiteralString],
) -> tuple[list[int], list[int]]:
    l1: list[int] = []
    l2: list[int] = []
    for x in spaced_entries:
        p1, p2 = map(int, x.split())
        l1.append(p1)
        l2.append(p2)
    return sorted(l1), sorted(l2)


def get_element_diff(l1: list[int], l2: list[int]) -> int:
    ans = sum(map(lambda x: abs(x[0] - x[1]), zip(l1, l2)))
    return ans


def wavg(l1: list[int], l2: list[int]) -> int:
    ans = sum(map(lambda x: l2.count(x) * x, l1))
    return ans


def part1():
    print("AoC 2024: 1.1")
    tl = """3   4
4   3
2   5
1   3
3   9
3   3""".split(
        "\n"
    )
    l1, l2 = get_locations_lists(tl)
    ans = get_element_diff(l1, l2)
    assert ans == 11
    l1, l2 = get_locations_lists(al)
    ans = get_element_diff(l1, l2)
    print("Part 1:", ans)
    assert ans == 2166959


def part2():
    print("AoC 2024: 1.2")
    tl = """3   4
4   3
2   5
1   3
3   9
3   3""".split(
        "\n"
    )
    l1, l2 = get_locations_lists(tl)
    ans = wavg(l1, l2)
    assert ans == 31, f"{ans} != 31"
    l1, l2 = get_locations_lists(al)
    ans = wavg(l1, l2)
    print("Part 2:", ans)
    assert ans == 23741109, f"{ans} != 23741109"


if __name__ == "__main__":
    part1()
    part2()

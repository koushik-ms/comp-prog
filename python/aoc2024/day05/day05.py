from collections.abc import Sequence
from typing import LiteralString
from .p01 import al


def part1():
    print("AoC 2024: 5.1")
    por, ul = (
        """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split(
            "\n\n"
        )
    )
    por, ul = al
    ordering: dict[int, set[int]] = {}
    for rule in por.splitlines():
        pred, succ = list(map(int, rule.split("|")))
        if pred not in ordering.keys():
            ordering[pred] = set()
        ordering[pred].add(succ)
    # print(f"Ordering: {ordering}")

    ans = 0
    for u in ul.splitlines():
        pages = list(map(int, u.split(",")))
        pp: set[int] = set()
        mc = True
        for page in pages:
            wop = pp.intersection(ordering.get(page, set()))
            if len(wop):
                # print(f"Violation for {page}, {pp}, {wop}")
                mc = False
                break
            pp.add(page)
        if mc:
            # print(f"Adding manual {u} to safe list.")
            ans += pages[len(pages) // 2]
    print("Part 1:", ans)
    assert ans == 5091, f"Expected: 5091 vs {ans}"


def part2():
    print("AoC 2024: 5.2")
    por, ul = (
        """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split(
            "\n\n"
        )
    )
    por, ul = al
    ordering: dict[int, set[int]] = {}
    for rule in por.splitlines():
        pred, succ = list(map(int, rule.split("|")))
        if pred not in ordering.keys():
            ordering[pred] = set()
        ordering[pred].add(succ)
    # print(f"Ordering: {ordering}")

    ans: int = 0
    for u in ul.splitlines():
        pages = list(map(int, u.split(",")))
        pp: set[int] = set()
        mc = True
        for page in pages:
            wop = pp.intersection(ordering.get(page, set()))
            if len(wop):
                # print(f"Violation for {page}, {pp}, {wop}")
                mc = False
                break
            pp.add(page)
        if not mc:
            # print(f"re-ordering unsafe manual {u}")
            im = [len(ordering.get(page, set()).intersection(pages)) for page in pages]
            # print(f"Index map: {im}")
            np = [0] * len(pages)
            for i in range(len(pages)):
                np[im[i]] = pages[i]
            # print(f"Reordered list: {np}")
            ans += np[len(np) // 2]
    print("Part 2:", ans)
    assert ans == 4681, f"Expected: 4681 vs {ans}"


if __name__ == "__main__":
    part1()
    part2()

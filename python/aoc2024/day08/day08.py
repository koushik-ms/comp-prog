from .sol import solve


def part1():
    print("AoC 2024: 8.1")
    tl = open("day08/08.in").readlines()
    ans = solve(tl)
    assert ans == 14, f"Expected: 14 vs {ans}"
    al = open("day08/08.txt").readlines()
    ans = solve(al)
    print("Part 1:", ans)
    assert ans == 318, f"Expected: 318 vs {ans}"


def part2():
    print("AoC 2024: 8.2")
    tl = open("day08/08.in").readlines()
    ans = solve(tl, part2=True)
    assert ans == 34, f"Expected: 34 vs {ans}"
    al = open("day08/08.txt").readlines()
    ans = solve(al, part2=True)
    print("Part 2:", ans)
    assert ans == 1126, f"Expected: 1126 vs {ans}"


if __name__ == "__main__":
    part1()
    part2()

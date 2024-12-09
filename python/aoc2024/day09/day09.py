from .sol import solve


def part1():
    print("AoC 2024: 9.1")
    tl = open("day09/09.in").read().strip()
    ans = solve(tl)
    assert ans == 1928, f"Expected: 1928 vs {ans}"
    al = open("day09/09.txt").read().strip()
    ans = solve(al)
    print("Part 1:", ans)
    assert ans == 6435922584968, f"Expected: 6435922584968 vs {ans}"


def part2():
    print("AoC 2024: 9.2")
    tl = open("day09/09.in").read().strip()
    ans = solve(tl, part2=True)
    assert ans == 2858, f"Expected: 2858 vs {ans}"
    al = open("day09/09.txt").read().strip()
    ans = solve(al, part2=True)
    print("Part 2:", ans)
    assert ans == 6469636832766, f"Expected: 6469636832766 vs {ans}"


if __name__ == "__main__":
    part1()
    part2()

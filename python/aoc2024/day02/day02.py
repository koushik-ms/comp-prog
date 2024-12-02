from .p01 import al


def test_rules(rep: list[int]):
    reps = sorted(rep)
    repr = sorted(rep, reverse=True)
    if reps != rep and repr != rep:
        return False
    ad: list[int] = [abs(rep[i] - rep[i - 1]) for i in range(1, len(rep))]
    if min(ad) < 1 or max(ad) > 3:
        return False
    return True


def test_rules_part2(rep: list[int]):
    if test_rules(rep):
        return True
    for i in range(len(rep)):
        nrep = rep[0:i] + rep[i + 1 :]
        if test_rules(nrep):
            return True
    return False


def part1():
    print("AoC 2024: 2.1")
    tl = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split(
        "\n"
    )
    ans = sum(test_rules(list(map(int, r.split()))) for r in tl)
    assert ans == 2
    ans = sum(test_rules(list(map(int, r.split()))) for r in al)
    print("Part 1:", ans)
    assert ans == 585


def part2():
    print("AoC 2024: 2.2")
    tl = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split(
        "\n"
    )
    ans = sum(test_rules_part2(list(map(int, r.split()))) for r in tl)
    assert ans == 4, f"expected: 4, actual: {ans}"
    ans = sum(test_rules_part2(list(map(int, r.split()))) for r in al)
    print("Part 2:", ans)
    assert ans == 626, f"Expected: 626, actual: {ans}"


if __name__ == "__main__":
    part1()
    part2()

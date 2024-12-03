from .p01 import al
import re


def part1():
    print("AoC 2024: 3.1")
    tl = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""  # print("Part 1:", ans)
    pattern = r"mul\((\d+),(\d+)\)"
    ans = sum(int(x) * int(y) for x, y in re.findall(pattern, tl))
    assert ans == 161, f"Expected: 161 vs {ans}"
    ans = sum(int(x) * int(y) for x, y in re.findall(pattern, al))
    print("Part 1:", ans)
    assert ans == 175615763, f"Expected: 175615763 vs {ans}"


def do_only_do_muls(text: str) -> int:
    pat = r"(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))"
    ans = 0
    count = True
    for sub, x, y in re.findall(pat, text):
        if sub == "do()":
            count = True
        elif sub == "don't()":
            count = False
        elif count:
            ans += int(x) * int(y)
    return ans


def part2():
    print("AoC 2024: 3.2")
    tl = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""  # print("Part 1:", ans)
    ans = do_only_do_muls(tl)
    assert ans == 48, f"Expected: 48 vs {ans}"
    ans = do_only_do_muls(al)
    print("Part 2:", ans)
    assert ans == 74361272, f"Expected: 74361272 vs {ans}"


if __name__ == "__main__":
    part1()
    part2()

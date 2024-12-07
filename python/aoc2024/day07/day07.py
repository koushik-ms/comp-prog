from typing import LiteralString
from .p01 import al


def part1():
    print("AoC 2024: 7.1")
    tl = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split(
        "\n"
    )
    ans = sum_valid_ops(tl)
    assert ans == 3749, f"Expected: 3749 vs {ans}"
    ans = sum_valid_ops(al)
    print("Part 1:", ans)
    assert ans == 10741443549536, f"Expected: 10741443549536 vs {ans}"


def sum_valid_ops(cl: list[LiteralString], part2: bool = False) -> int:
    def cal(entry: str):
        res, ops = entry.strip().split(":")
        res = int(res)
        vals = [int(v) for v in ops.strip().split()]
        return res * can_eval(vals, res, part2)

    return sum(cal(l) for l in cl)


def can_eval(operands: list[int], desired_result: int, part2=False) -> bool:
    def eval_rest(desired_value, ro: list[int]) -> bool:
        if len(ro) == 1:
            return desired_value == ro[0]
        last = ro[-1]
        head = ro[:-1]
        if desired_value % last == 0 and eval_rest(desired_value // last, head):
            return True
        if desired_value > last and eval_rest(desired_value - last, head):
            return True
        if part2:
            last_str = str(last)
            dv_str = str(desired_value)
            if (
                len(dv_str) > len(last_str)
                and dv_str.endswith(last_str)
                and eval_rest(int(dv_str[: -len(last_str)]), head)
            ):
                return True
        return False

    return eval_rest(desired_result, operands)


def part2():
    print("AoC 2024: 7.2")
    tl = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split(
        "\n"
    )
    ans = sum_valid_ops(tl, part2=True)
    assert ans == 11387, f"Expected: 11387 vs {ans}"
    ans = sum_valid_ops(al, part2=True)
    print("Part 2:", ans)
    assert ans == 500335179214836, f"Expected: 500335179214836 vs {ans}"


if __name__ == "__main__":
    part1()
    part2()

from tqdm import tqdm
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
    part1_ops = [
        lambda x, y: x + y,
        lambda x, y: x * y,
    ]

    ans = sum_valid_ops(tl, valid_ops=part1_ops)
    assert ans == 3749, f"Expected: 3749 vs {ans}"
    ans = sum_valid_ops(al, valid_ops=part1_ops)
    print("Part 1:", ans)
    assert ans == 10741443549536, f"Expected: 10741443549536 vs {ans}"


def sum_valid_ops(cl, valid_ops=[]) -> int:
    def cal(entry):
        res, ops = entry.strip().split(":")
        res = int(res)
        vals = list(map(int, ops.strip().split()))
        return res * can_eval(vals, res, valid_ops)

    return sum(cal(l) for l in tqdm(cl))


def can_eval(operands: list[int], desired_result: int, valid_ops=[]) -> bool:
    def eval_rest(starting_value=0, ro: list[int] = None) -> bool:
        if len(ro) == 0:
            return starting_value == desired_result
        return any(eval_rest(op(starting_value, ro[0]), ro[1:]) for op in valid_ops)

    return eval_rest(0, operands)


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
    part2_ops = [
        lambda x, y: x + y,
        lambda x, y: x * y,
        lambda x, y: int(str(x) + str(y)),
    ]
    ans = sum_valid_ops(tl, valid_ops=part2_ops)
    assert ans == 11387, f"Expected: 11387 vs {ans}"
    ans = sum_valid_ops(al, valid_ops=part2_ops)
    print("Part 2:", ans)
    assert ans == 500335179214836, f"Expected: 500335179214836 vs {ans}"


if __name__ == "__main__":
    part1()
    part2()

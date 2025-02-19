from functools import cache

tcl, pal = open(0).read().split("\n\n")

towel_codes = tuple(tcl.split(", "))
patterns = pal.splitlines()


@cache
def is_possible(pattern: str, codes: tuple[str], si: int = 0) -> int:
    if si >= len(pattern):
        return True
    return sum(
        pattern.startswith(code, si) and is_possible(pattern, codes, si + len(code))
        for code in codes
    )


ans = sum(is_possible(x, towel_codes) for x in patterns)
print(f"Ans: {ans}")

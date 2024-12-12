from functools import cache

l = open(0).read()
nums = [int(x.strip()) for x in l.strip().split()]


@cache
def get_len(n: int, ic: int = 25) -> int:
    if ic == 0:
        return 1
    if n == 0:
        return get_len(1, ic - 1)
    str_n = str(n)
    len_n = len(str_n)
    if len_n % 2 == 0:
        return get_len(int(str_n[: len_n // 2]), ic - 1) + get_len(
            int(str_n[len_n // 2 :]), ic - 1
        )
    return get_len(n * 2024, ic - 1)


ans = 0
for n in nums:
    ans += get_len(n, 75)

print(ans)

from .p01 import al

def part1():
    print("AoC 2023: 6.1")
    tl = """Time:      7  15   30
Distance:  9  40  200""".split("\n")
    # ts = [(7, 9), (15, 40), (30, 200)]
    print(pin(parse(tl)))
    print(pin(parse(al)))

def part2():
    print("AoC 2023: 6.2")
    tl = """Time:      7  15   30
Distance:  9  40  200""".split("\n")
    print(farse(tl))
    print(pin(farse(tl)))
    print(pin(farse(al)))

def farse(l):
    res = []
    for x in l:
        vals = x.split(":")[-1].strip()
        res.append([int(''.join(vals.split()))])
    return list(zip(*res))

def parse(l):
    res = []
    for x in l:
        vals = x.split(":")[-1].strip()
        res.append([int(p) for p in vals.split()])
    return list(zip(*res))

def pin(l):
    res = 1
    for x, y in l:
        res = res * bs(x, y)
    return res

def bs(t, s):
    l = 0
    r = t//2
    while l<r:
        p = (l+r)//2
        f = p * (t-p)
        # print(f">> {l}, {r}, {p} {f} ({s} for {t})")
        if f > s:
            r = p
        else:
            l = p+1
    return t - 2*r + 1

if __name__ == "__main__":
    part2()

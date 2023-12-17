from .p01 import al

def part1():
    print("AoC 2023: 4.1")
    ts = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    print(gl(ts))
    print(val(ts))
    tl = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")
    print(sum([val(ts) for ts in tl]))
    print(sum([val(ts) for ts in al]))

def part2():
    print("AoC 2023: 4.2")
    tl = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")
    print(spv(tl))
    print(spv(al))

def spv(tl):
    cc = {}
    for c in tl:
        cn = int(c.split(": ")[0].split()[-1].strip())
        cc[cn] = cc.get(cn, 0) + 1
        for i in range(nw(c)):
            cc[cn + i + 1] = cc.get(cn+i+1, 0) + cc[cn]
    return sum(cc.values())

def val(ts):
    j = nw(ts)
    return 2**(j-1) if j>0 else 0

def nw(ts):
    wl, al = gl(ts)
    return len([e for e in al if e in wl])

def gl(ts):
    wl, al = ts.split(": ")[-1].strip().split("|")
    return wl.strip().split(), al.strip().split()

if __name__ == "__main__":
    part2()

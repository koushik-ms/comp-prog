import re
from p01 import al

def cm(rec, counts):
    # rec, counts = (x.strip() for x in s.split())
    ps = r"^\.*"
    ps += r"\.+".join([r"\#{" + i + r"}" for i in counts.split(",")])
    ps += "\.*$"
    pat = re.compile(ps)
    nq = rec.count("?")
    # print(ps, nq)
    ans = 0
    for i in range(2**nq):
        q = 0
        candidate = ""
        for c in rec:
            if c == "?":
                candidate += "#" if (i & 2**q) else "."
                q += 1
            else:
                candidate += c
        # print(candidate, end = "")
        if pat.fullmatch(candidate):
            # print("  == > Match!")
            ans += 1
        # else:
        #     print("skip")
    return ans


def fc(l):
    ans = 0
    for s in l:
        rec, counts = (x.strip() for x in s.split())
        ans += cm(rec, counts)
    return ans

def part1():
    print("AoC 2023: 12.1")
    ts = "?###???????? 3,2,1"
    print(cm(*ts.split()))
    tl = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split("\n")
    print(fc(tl))
    # print(fc(al))

def part2():
    print("AoC 2023: 12.2")
    ts = "?###???????? 3,2,1"
    rec, counts = ts.split()
    rec = "?".join([rec]*5)
    counts = ",".join([counts]*5)
    print(cm(rec, counts))


if __name__ == "__main__":
    part1()
    part2()

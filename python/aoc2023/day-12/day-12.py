import re
from p01 import al
from functools import cache

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


def dm(rec, cs):
    @cache
    def em(curr = 0, bi = 0, run = 0):
        l = len(rec)
        # print(f"{rec=}, {counts=}, {curr=}, {bi=}, {run=}")
        if curr >= l:
            if (
                (run == 0 and bi == len(counts))
                or (bi == len(counts)-1 and run == counts[bi])
            ):
                return 1
            else:
                return 0
        ch = rec[curr]
        if ch == ".":
            if run == 0 or (bi < len(counts) and run == counts[bi]):
                if bi < len(counts) and run == counts[bi]:
                    bi += 1
                    run = 0
                return em(curr+1, bi, run)
            return 0
        if ch == "#":
            return em(curr+1, bi, run+1)
        if ch == "?":
            pa = em(curr+1, bi, run+1)
            if run == 0 or (bi < len(counts) and run == counts[bi]):
                if bi < len(counts) and run == counts[bi]:
                    bi += 1
                    run = 0
                pa += em(curr+1, bi, run)
            return pa
    counts = [int(c.strip()) for c in cs.split(",")]
    return em()

def fc(l, cm=cm):
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
    print(fc(al, cm=dm))

def part2():
    print("AoC 2023: 12.2")
    ts = "?###???????? 3,2,1"
    rec, counts = ts.split()
    rec = "?".join([rec]*5)
    counts = ",".join([counts]*5)
    print(rec, counts)
    print(dm(rec, counts))
    tl = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split("\n")
    # tl = replicate(tl)
    # print("\n".join(replicate(tl)))
    print(fc(replicate(tl), cm=dm))
    print(fc(replicate(al), cm=dm))

def replicate(l):
    ans = []
    for s in l:
        rec, counts = (x.strip() for x in s.split())
        ans.append(f'{"?".join([rec]*5)} {",".join([counts]*5)}')
    return ans


if __name__ == "__main__":
    part1()
    part2()

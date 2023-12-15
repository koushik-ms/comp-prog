from p01 import al
from collections import defaultdict

def part1():
    print("AoC 2023: 15.1")
    ts = "HASH"
    print(h(ts))
    tl = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    print(p(tl))
    print(p(al))

def part2():
    print("AoC 2023: 15.2")
    tl = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    print(q(tl))
    print(q(al))

def q(st):
    b = {} # defaultdict(defaultdict(list))
    for s in st.split(","):
        label = s[:-1] if s[-1] == "-" else s[:-2]
        fl = s[-1]
        k = h(label)
        if fl == "-":
            if k in b and label in b[k]:
                del b[k][label]
        else:
            if k in b:
                b[k][label] = int(fl)
            else:
                b[k] = {label: int(fl)}
    ans = 0
    # print(b)
    for i in b:
        j = 0
        for label, fl in b[i].items():
            ans += (i+1) * (j+1) * fl
            # print(type(i), i, type(j), j, type(fl), fl, "=>", ans)
            j += 1
    return ans

def p(st):
    ans = 0
    for l in st.splitlines():
        ans += sum([h(s) for s in l.split(",")])
    return ans

def h(s):
    ans = 0
    for c in s:
        ans += ord(c)
        ans *= 17
        ans %= 256
    return ans

if __name__ == "__main__":
    part1()
    part2()

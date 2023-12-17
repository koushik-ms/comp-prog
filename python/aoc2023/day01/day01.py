from .p01 import al

def part1():
    print("AoC 2023: 1.1")
    print(val("pqr3stu8vwx"))
    assert(val("pqr3stu8vwx") == 38)
    tl = ["1abc2", "pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
    print(cvs(tl))
    assert(cvs(tl) == 142)
    print(al[0:3], al[-3:])
    print(cvs(al))

def part2():
    print("AoC 2023: 1.2")
    print(cal("131"))
    print(cal("sevenine"))
    tl = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split("\n")
    print(cvs(tl, cal))
    print(al[0:3], al[-3:])
    print(cvs(al, cal))

v = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
tokens = "1 2 3 4 5 6 7 8 9 0 one two three four five six seven eight nine".split()
def cal(s):
    def f(c):
        if c in v:
            return v[c]
        else:
            return c
    ind = [(s.find(e), e) for e in tokens]
    fin = sorted([e for e in ind if e[0] >= 0])
    ind = [(s.rfind(e), e) for e in tokens]
    rin = sorted([e for e in ind if e[0] >= 0])
    r = f(fin[0][-1]) + f(rin[-1][-1])
    return int(r)

def val(s):
    ns = [c for c in s if c.isnumeric()]
    return int(ns[0] + ns[-1])

def cvs(l, op=val):
    return sum([op(e) for e in l])

if __name__ == "__main__":
    part2()

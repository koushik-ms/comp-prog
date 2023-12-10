from p01 import al

def part1():
    print("AoC 2023: 2.1")
    ts = "3 blue, 4 red"
    print(counts(ts))
    ts = "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    print(maxes(ts))
    ts = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    print(id_or_0(ts))
    tl = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split("\n")
    print(sum([id_or_0(e) for e in tl]))
    print(sum([id_or_0(e) for e in al]))

def part2():
    print("AoC 2023: 2.2")
    ts = "3 blue, 4 red"
    print(counts(ts))
    ts = "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    print(maxes(ts))
    ts = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    print(power(ts))
    tl = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split("\n")
    print(sum([power(e) for e in tl]))
    print(sum([power(e) for e in al]))

def power(s):
    t, ss = s.split(": ")
    m = maxes(ss)
    res = 1
    for k in m:
        res = res * m[k]
    return res

avl = {"blue": 14, "red": 12, "green": 13}
def id_or_0(s):
    t, ss = s.split(": ")
    res = maxes(ss)
    for k in res:
        if res[k] > avl[k]:
            return 0
    return int(t.split()[-1])

def maxes(s):
    res = {"blue": 0, "red": 0, "green": 0}
    for g in s.split(";"):
        for k,v in counts(g).items():
            res[k] = max(v, res[k])
    return res

def counts(s):
    res = {}
    for x in s.split(","):
        (n, c) = x.strip().split()
        res[c] = int(n)
    return res

if __name__ == "__main__":
    part2()

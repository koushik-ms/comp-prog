from .p01 import al

def score(hand):
    counts ={k: hand.count(k) for k in set(hand)}
    s = sorted(counts.values(), reverse=True)
    if s[0] > 3:
        return 2 + s[0]
    if s[0] > 1:
        return 4+s[0]-len(s)
    return 1

def score2(hand):
    sh = hand.replace("J", "")
    counts ={k: sh.count(k) for k in set(sh)}
    s = sorted(counts.values(), reverse=True)
    if s:
        s[0] += hand.count("J")
    else:
        s = [hand.count("J")]
    if s[0] > 3:
        return 2 + s[0]
    if s[0] > 1:
        return 4+s[0]-len(s)
    return 1

kinds = "23456789TJQKA"
rep = [
    ("J", "U"),
    ("Q", "V"),
    ("K", "W"),
    ("A", "X"),
]

def repl(s):
    for o, n in rep:
        s = s.replace(o, n)
    return s

rep2 = [
    ("J", "1"),
    ("Q", "V"),
    ("K", "W"),
    ("A", "X"),
]

def repl2(s):
    for o, n in rep2:
        s = s.replace(o, n)
    return s

def tf(x, scoring_function = score, rf = repl):
    hand, bid = (v.strip() for v in x.split())
    return (scoring_function(hand),rf(hand), hand, int(bid))

def score_and_sort(l, scoring_function = score, rf = repl):
    a = [tf(x, scoring_function = scoring_function, rf=rf) for x in l]
    return sorted(a)

def points(ts, scoring_function = score, rf=repl):
    res = 0
    for i, t in enumerate(score_and_sort(ts, scoring_function=scoring_function, rf=rf)):
        res += (i+1) * t[-1]
    return res

def part1():
    print("AoC 2023: 7.1")
    tl = ["AAAAA", "AA8AA", "23332", "TTT98", "23432", "A23A4", "23456"]
    print([score(x) for x in tl])
    tl = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split("\n")
    print(points(tl))
    print(points(al))

def part2():
    print("AoC 2023: 7.2")
    tl = ["AAAAA", "AA8AA", "23332", "TTT98", "23432", "A23A4", "23456"]
    print([score2(x) for x in tl])
    tl = ["JJJJJ", "QJJQ2", "T55J5", "KTJJT", "QQQJA"]
    print([score2(x) for x in tl])
    tl = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split("\n")
    print(points(tl, scoring_function=score2, rf=repl2))
    print(points(al, scoring_function=score2, rf=repl2))

if __name__ == "__main__":
    part2()

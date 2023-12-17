from .p01 import al


def score(hand):
    """ Score a hand

    Count and sort descending by frequency
    [5] => five of a kind
    [4, 1] => four of a kind
    [3, 2] => full house
    [3, 1, 1] => Three of a kind
    [2, 2, 1] => Two pair
    [2, 1, 1, 1] => One pair
    [1, 1, 1, 1, 1] => High Card
    """
    counts = {k: hand.count(k) for k in set(hand)}
    s = sorted(counts.values(), reverse=True)
    if s[0] > 3:
        return 2 + s[0]
    if s[0] > 1:
        return 4 + s[0] - len(s)
    return 1


def score2(hand):
    """ Score a hand with Joker rules

    Unless the hand is made up of Jokers add count of Jokers
    to the card with highest count. Then use the same rules
    as normal scoring function.
    """
    sh = hand.replace("J", "")
    counts = {k: sh.count(k) for k in set(sh)}
    s = sorted(counts.values(), reverse=True)
    if s:
        s[0] += hand.count("J")
    else:
        s = [hand.count("J")]
    if s[0] > 3:
        return 2 + s[0]
    if s[0] > 1:
        return 4 + s[0] - len(s)
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


def tf(x, scoring_function=score, ranking_function=repl):
    hand, bid = (v.strip() for v in x.split())
    return (scoring_function(hand), ranking_function(hand), hand, int(bid))


def score_and_sort(l, scoring_function=score, ranking_function=repl):
    a = [
        tf(x, scoring_function=scoring_function, ranking_function=ranking_function)
        for x in l
    ]
    return sorted(a)


def points(ts, scoring_function=score, ranking_funcion=repl):
    res = 0
    for i, t in enumerate(
        score_and_sort(
            ts, scoring_function=scoring_function, ranking_function=ranking_funcion
        )
    ):
        res += (i + 1) * t[-1]
    return res


def part1():
    print("AoC 2023: 7.1")
    tl = ["AAAAA", "AA8AA", "23332", "TTT98", "23432", "A23A4", "23456"]
    print([score(x) for x in tl])
    tl = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split(
        "\n"
    )
    pt = points(tl)
    print(pt)
    assert pt == 6440
    pa = points(al)
    print(pa)
    assert pa == 251106089


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
QQQJA 483""".split(
        "\n"
    )
    pt = points(tl, scoring_function=score2, ranking_funcion=repl2)
    print(pt)
    assert pt == 5905
    pa = points(al, scoring_function=score2, ranking_funcion=repl2)
    print(pa)
    assert pa == 249620106


if __name__ == "__main__":
    part1()
    part2()

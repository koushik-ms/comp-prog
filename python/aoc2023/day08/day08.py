import math
from .p01 import al


def dec(ts):
    instructions, netlist = (v.strip() for v in ts)
    network = {}
    for l in netlist.split("\n"):
        src, pos = l.strip().split(" = ")
        l, r = pos.strip("() ").split(", ")
        network[src] = (l, r)
    return instructions, network


def steps(loc, instructions, network, ef):
    count = 0
    l = len(instructions)
    while not ef(loc):
        if (instructions[count % l]) in "lL":
            loc = network[loc][0]
        else:
            loc = network[loc][1]
        count += 1
    return count


def navigate1(ts):
    i, n = dec(ts)
    return steps("AAA", i, n, ef=lambda loc: loc == "ZZZ")


def navigate2(ts):
    i, n = dec(ts)
    loc = [x for x in n.keys() if x.endswith("A")]
    a = [steps(x, i, n, ef=lambda loc: loc.endswith("Z")) for x in loc]
    return math.lcm(*a)


def part1():
    print("AoC 2023: 8.1")
    ts = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".split(
        "\n\n"
    )
    print(navigate1(ts))
    ts = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".split(
        "\n\n"
    )
    print(navigate1(ts))
    print(navigate1(al))


def part2():
    print("AoC 2023: 8.2")
    tl = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split(
        "\n\n"
    )
    print(navigate2(tl))
    print(navigate2(al))


if __name__ == "__main__":
    part1()
    part2()

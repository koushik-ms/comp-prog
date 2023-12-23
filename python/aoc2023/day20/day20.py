from collections import defaultdict
from functools import reduce
from .p01 import al

def config(s):
    modules = {}
    for l in s:
        tn, outs = l.split(" -> ")
        t, n = tn[0], tn[1:]
        modules[n] = { "type": t, "outs": outs.split(", ") }
    return modules

# 0 -> low, 1 -> high
def init(mods):
    # print(f"{mods=}")
    inp = {}
    for m in mods:
        if mods[m]["type"] == "%":
            inp[m] = 0
        if mods[m]["type"] == "&":
            inp[m] = {k: 0 for k in mods if m in mods[k]["outs"]}
    return inp

def cp(s):
    def ffs():
        return {m: states[m] for m in states if mods[m]["type"] == "%"}
    mods = config(s)
    states = init(mods)
    initial_states = ffs()
    cl = 0
    cm = "roadcaster"
    cp = defaultdict(int)
    # print("="*80)
    # print(f"{initial_states=}")
    while True:
        pp: list[tuple[int, str, str]] = [(0, cm, "button")]
        while pp:
            p, mn, src = pp.pop(0)
            cp["high" if p else "low"] += 1
            if mn in mods:
                m = mods[mn]
                if m["type"] == "b":
                    for o in m["outs"]:
                        pp.append((p, o, mn))
                if m["type"] == "%":
                    if not p:
                        states[mn] = 1 if (states[mn] == 0) else 0
                        op = 1 if (states[mn] == 1) else 0
                        for o in m["outs"]:
                            pp.append((op, o, mn))
                if m["type"] == "&":
                    states[mn][src] = p
                    op = 0 if all([x==1 for x in states[mn].values()]) else 1
                    for o in m["outs"]:
                        pp.append((op, o, mn))
            # print(f"{cl=}>>{src}-{p}->{mn} : {cp=} {pp=}")
        cl += 1
        curr_states = ffs()
        # print(f"{cl=}: {curr_states=}, {initial_states=}")
        if curr_states == initial_states or cl >= 1000:
            break
    return reduce(lambda x,y: x*y, cp.values())*(1000000//(cl*cl))


def rx(s):
    mods = config(s)
    states = init(mods)
    initial_states = init(mods)
    cycle_lengths = defaultdict(int)
    cycles = defaultdict(list)
    cl = 1
    cp = defaultdict(int)
    while True:
        pp: list[tuple[int, str, str]] = [(0, "roadcaster", "button")]
        while pp:
            p, mn, src = pp.pop(0)
            if mn == "rx" and p == 0:
                return cl
            cp["high" if p else "low"] += 1
            if mn in mods:
                m = mods[mn]
                if m["type"] == "b":
                    for o in m["outs"]:
                        pp.append((p, o, mn))
                if m["type"] == "%":
                    if not p:
                        states[mn] = 1 if (states[mn] == 0) else 0
                        op = 1 if (states[mn] == 1) else 0
                        if states[mn] == initial_states[mn] and cl not in cycles[mn]:
                            cycles[mn].append(cl)
                            cycle_lengths[mn] = cycles[mn][-1] - (cycles[mn][-2] if len(cycles[mn]) > 1 else 0)
                        # if "rx" in m["outs"]:
                        #     print(f"Send {op} to rx")
                        for o in m["outs"]:
                            pp.append((op, o, mn))
                if m["type"] == "&":
                    states[mn][src] = p
                    op = 0 if all([x==1 for x in states[mn].values()]) else 1
                    if all(x==0 for x in states[mn].values()) and cl not in cycles[mn]:
                        cycles[mn].append(cl)
                        cycle_lengths[mn] = cycles[mn][-1] - (cycles[mn][-2] if len(cycles[mn]) > 1 else 0)
                    # if "rx" in m["outs"]:
                    #     print(f"Send {op} to rx")
                    for o in m["outs"]:
                        pp.append((op, o, mn))
            # print(f"{cl=}>>{src}-{p}->{mn} : {cp=} {pp=}")
        cl += 1
        # if cl%100 == 0:
        #     print(f"{cl=}: {states=}, {initial_states=}")
        if states == initial_states or cl >= 5000:
            break
    # Even 5000 cycles is not enough to send low pulse to rx. Below code 
    # renders a digraph in dot language which can be rendered via graphviz
    # or online (e.g., https://edotor.net/)
    # Based on this we know that four nodes drive "lg" which drives "rx"
    # Thus we compute the number of cycles needed to drive these inputs to
    # send low pulse. Then number of cycles to drive all of them at the same
    # time is the LCM of these cycle_lengths. These numbers are apparently
    # co-prime, thus their LCM is their product.
    # print("\n\ndigraph {")
    # for m in mods:
    #     ss = f"{mods[m]['type']}{m}"
    #     print(f'\t{m}[label="{ss}"]')
    #     for o in mods[m]["outs"]:
    #         ds = f"{mods[o]['type']}{o}" if o in mods else "?"+o
    #         print(f"\t{m} -> {o}")
    # print("}")
    return reduce(lambda x,y: x*y, [ cycle_lengths[x] for x in ["vc", "ls", "nb", "vg"]])

def part1():
    print("AoC 2023: 20.1")
    tl = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a""".split("\n")
    pt = cp(tl)
    print(pt)
    assert pt == 32000000
    tl = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output""".split("\n")
    pt = cp(tl)
    print(pt)
    assert pt == 11687500
    pa = cp(al)
    print(pa)
    assert pa == 929810733


def part2():
    print("AoC 2023: 20.2")
    pa = rx(al)
    print(pa)
    assert pa == 231657829136023



if __name__ == "__main__":
    part1()
    part2()

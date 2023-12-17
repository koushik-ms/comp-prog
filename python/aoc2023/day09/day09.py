from .p01 import al

def part1():
    print("AoC 2023: 9.1")
    print(adjacent_difference([3, 6, 9]))
    print(adjacent_difference([3, 3, 3]))
    assert(set(adjacent_difference([3, 3, 3])) == set([0]))
    print(predict([0, 3, 6, 9, 12, 15]))
    tl = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".split("\n")
    print(spv(tl))
    print(spv(al))

def part2():
    print("AoC 2023: 9.2")
    print(rpv(al))

def rpv(l):
    return sum(predict([int(n) for n in reversed(s.split())]) for s in l)

def spv(l):
    return sum(predict([int(n) for n in s.split()]) for s in l)

def predict(l):
    n = adjacent_difference(l)
    if set(n) == set([0]):
        return l[-1]
    return l[-1] + predict(n)

def adjacent_difference(l):
    if len(l) < 2:
        return [0]
    return [l[i+1] - l[i] for i in range(len(l)-1)]

if __name__ == "__main__":
    part1()
    part2()

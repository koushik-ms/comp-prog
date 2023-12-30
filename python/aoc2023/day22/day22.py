from collections import defaultdict
from functools import reduce
from heapq import heappop, heappush
from time import sleep
from .p01 import al


def process(pos_list):
    # TODO: Sort list based on smaller z co-ordinate
    intdict = lambda : defaultdict(int)
    sorted_pos = []
    earth = defaultdict(intdict)
    bo = defaultdict(intdict)
    settledat = {}
    unshakeables = set()
    for pos in pos_list:
        start, end = pos.split("~")
        sx, sy, sz = [int(p) for p in start.split(",")]
        ex, ey, ez = [int(p) for p in end.split(",")]
        heappush(sorted_pos, (sz, (sx, sy, sz), (ex, ey, ez)))
    i = 0
    while sorted_pos:
        i += 1
        _, (sx, sy, sz), (ex, ey, ez) = heappop(sorted_pos)
        tz = 0
        posz = set()
        so = set()
        for x in range(sx, ex+1):
            for y in range(sy, ey+1):
                posz.add(earth[x][y])
                if earth[x][y] > tz:
                    tz = earth[x][y]
                    so = set([bo[x][y]])
                elif earth[x][y] == tz and earth[x][y] != 0:
                    so.add(bo[x][y])
        # tz = max(posz) if posz else sz
        for x in range(sx, ex+1):
            for y in range(sy,ey+1):
                earth[x][y] = tz + (ez-sz+1)
                bo[x][y] = i # In bo, zero means no block, x means x-1th block
        ns = tz+1
        ne = tz + (ez-sz+1)
        settledat[i] = ((sx, sy, ns), (ex, ey, ne), list(so))
        # print(f'{sx},{sy},{sz}~{ex},{ey},{ez} {tz=} |> settles {sx},{sy},{ns}~{ex},{ey},{ne} {so=}')
        # print(f'         => {earth=}')
        if len(so) == 1:
            # print(f'{chr(ord("A")+i)} standing on {chr(ord("A")+list(so)[0]-1)}')
            unshakeables = unshakeables.union(so)
    return settledat, unshakeables

def zs(l):
    _, u = process(l)
    return len(l) - len(u)


def bc(l):
    s, u = process(l)
    n = len(l)
    ans = 0
    for i in range(1, n+1):
        fb = [i]
        for j in range(1, n+1):
            if j == i:
                continue
            so = s[j][-1]
            # print(f'{i=}, {j=}, {s[j]=}')
            if so and all([x in fb for x in so]):
                fb.append(j)
                ans += 1
                # print(f'{i} => {j} which is {so} =>> {fb}')
    return ans

def part1():
    print("AoC 2023: 22.1")
    tl = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""".splitlines()
    pt = zs(tl)
    print(pt)
    assert pt == 5
    pa = zs(al)
    print(pa)
    assert pa == 405


def part2():
    print("AoC 2023: 22.2")
    tl = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""".splitlines()
    pa = bc(tl)
    print(pa)
    assert pa == 7
    pa = bc(al)
    print(pa)
    assert pa == 61297


if __name__ == "__main__":
    part1()
    part2()

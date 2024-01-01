from collections import defaultdict
from functools import reduce
from time import sleep
from math import gcd
from .p01 import al


def normalize(v):
    g = reduce(lambda x, y: gcd(x,y), v)
    return [int(x/g) for x in v]

def inter(pv1, pv2):
    loc1, vel1 = pv1
    loc2, vel2 = pv2
    x1, y1, _ = loc1
    x2, y2, _ = loc2
    vx1, vy1, _ = vel1
    vx2, vy2, _ = vel2
    D = vy1*vx2 - vx1*vy2
    Dt1 = (x1-x2)*vy2+(y2-y1)*vx2
    Dt2 = (y2-y1)*vx1 - (x2-x1)*vy1

    if D != 0:
        ct1 = Dt1/D
        ct2 = Dt2/D
        return [
            (True, ct1, (x1+vx1*ct1, y1+vy1*ct1, None)),
            (True, ct2, (x2+vx2*ct2, y2+vy2*ct2, None))
        ]
    # return [False, None, None]


    res = []
    if vx1 == 0 and vx2 == 0 and x1 == x2:
        ct1 = (y2-y1)/vy1 if vy1 else None
        ct2 = (y1-y2)/vy2 if vy2 else None
        if ct1 is not None or ct2 is not None:
            res.append([True, ct1 if ct1 is not None else ct2, (x1, None, None)]) # ordinate None => all possible values
            res.append([True, ct2 if ct2 is not None else ct1, (x2, None, None)]) # ordinate None => all possible values
        return res
    if vy1 == 0 and vy2 == 0 and y1 == y2:
        ct1 = (x2-x1)/vx1 if vx1 else None
        ct2 = (x1-x2)/vx2 if vx2 else None
        if ct1 is not None or ct2 is not None:
            res.append([True, ct1 if ct1 is not None else ct2, (None, y1, None)]) # abscissa None => all possible values
            res.append([True, ct2 if ct2 is not None else ct1, (None, y2, None)]) # abscissa None => all possible values
        return res

    m1, m2, c1, c2 = (None, None, None, None)
    type1, type2 = (True, True)
    if vx1 != 0:
        m1 = vy1 / vx1
        c1 = (y1 - m1*x1)
    elif vy1 != 0:
        type1 = False
        m1 = vx1 / vy1
        c1 = (x1 - m1*y1)
    if vx2 != 0:
        m2 = vy2 / vx2
        c2 = (y2 - m2*x2)
    elif vy1 != 0:
        type2 = False
        m2 = vx2 / vy2
        c2 = (x2 - m2*y2)
    if m1 == m2 and type1 == type2 :
        if c1 is not None and c2 is not None and c1 == c2:
            ct1 = None
            ct2 = None
            if vx1 != 0:
                ct1 = (x2-x1)/vx1
            elif vy1 != 0:
                ct1 = (y2-y1)/vy1
            if vx2 != 0:
                ct2 = (x1-x2)/vx2
            elif vy2 != 0:
                ct2 = (y1-y2)/vy2
            if ct1 is not None or ct2 is not None:
                return [
                    (True, ct1 if ct1 is not None else ct2, (None, None, None)),  # abscissa None => all possible values
                    (True, ct2 if ct2 is not None else ct1, (None, None, None))   # abscissa None => all possible values
                ]
        return [(False, None, None)]

    print(f"Uncovered corner case: {pv1=}, {pv2=}, {D=}")
    m1 = vy1 / vx1 if vx1 != 0 else None
    m2 = vy2 / vx2 if vx2 != 0 else None
    c1 = (y1 - m1*x1) if m1 is not None else None
    c2 = (y2 - m2*x2) if m2 is not None else None
    if m1 == m2:
        if c1 == c2:
            ct1 = tt(x1, y1, vx1, vy1, x2, y2)
            ct2 = tt(x2, y2, vx2, vy2, x1, y1)
            return [(True, ct1, (x2, y2, None)) ]
        if x1 == x2 and y1 == y2:
            return True, (x1, y1, None) # ?? what if this is outside range ?
        else:
            return False, None
    x0 = ((y2-m2*x2) - (y1-m1*x1))/(m1-m2)
    y0 = m1*x0 + y1 - m1*x1
    # print(f" ==> {m1=}, {m2=}, {x0=}, {y0=}")
    return True, (x0, y0, None)


def intersections(pvl, limx = [7, 27], limy = [7, 27]):
    repo = []
    ans = 0
    for pv in pvl:
        loc, vel = pv.strip().split(" @ ")
        loc = [int(m.strip()) for m in loc.strip().split(",")]
        vel = normalize([int(m.strip()) for m in vel.strip().split(",")])
        # print(f"{loc=}, {vel=}")
        repo.append((loc, vel))
    l = len(repo)
    for i in range(l):
        for j in range(i+1, l):
            ip = inter(repo[i], repo[j])
            # print(f"{i=}, {j=}: {repo[i]=}, {repo[j]=} ==> {ip=}")
            if all([x[0] and x[1]>=0 for x in ip]):
                # print(f"|> {i=} x {j=} Crossing: ", end="")
                cx, cy, _ = ip[0][-1]
                if cx is None or cy is None:
                    # print(f"Special Case!")
                    pass
                else:
                    if limx[0]<=cx<=limx[1] and limy[0]<=cy<=limy[1]:
                        # print("INSIDE!")
                        ans += 1
                    else:
                        # print("OUTSIDE!")
                        pass
    return ans

def part1():
    print("AoC 2023: 24.1")
    tl = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3""".splitlines()
    pt = intersections(tl)
    print(pt)
    assert pt == 2
    tl = """3, 0, 2 @ 0, 1, -2
3, 2, 5 @ 0, -1, -2
3, -1, 2 @ 0, -1, -2
5, 3, 0 @ -1, 2, -3
2, 0, 2 @ -1, 0, -2
3, 2, 2 @ 1, 1, -2""".splitlines()
    pt = intersections(tl)
    print(pt)
    assert pt == 0
    pa = intersections(al, limx=[200000000000000, 400000000000000], limy=[200000000000000, 400000000000000])
    print(pa)
    assert pa == 16018


def sum_pos(traj):
    # 3 co-ordinates, 3 velocities are unknown for the rock
    # rock hits all hailstones which means for every hailstone
    #   x + vx*t = x_rock + vx_rock * t
    #   ... and so on for y and z for same t
    # t is potentially different for each hailstone. Since we
    # have only  6 unknowns, we don't need all the input - either
    # the hailstones line up or they don't.
    # Each hailstone adds a time variable, so solving for 3 
    # hailstones is sufficient. We must use linear algebra, apparently
    # sympy is good at this. numpy would have also helped.
    import sympy
    x0, y0, z0, v0x, v0y, v0z = sympy.symbols('x0 y0 z0 v0x v0y v0z')
    t1, t2, t3 = sympy.symbols('t1 t2 t3')
    times = [t1, t2, t3]
    equations = []
    hs = [tuple(map(int, l.replace('@', ',').split(','))) for l in traj[:3]]
    for i in range(3):
        x, y, z, vx, vy, vz = hs[i]
        t = times[i]
        equations.append(x + t*vx - x0 - t*v0x)
        equations.append(y + t*vy - y0 - t*v0y)
        equations.append(z + t*vz - z0 - t*v0z)
    ans = sympy.solve(equations)
    return sum(ans[0][symbol] for symbol in [x0,y0,z0])

def part2():
    print("AoC 2023: 24.2")
    tl = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3""".splitlines()
    pt = sum_pos(tl)
    print(pt)
    assert pt == 47
    pa = sum_pos(al)
    print(pa)
    assert pa == 1004774995964534


if __name__ == "__main__":
    part1()
    part2()

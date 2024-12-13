import numpy
from numpy.linalg import solve

epsilon = 0.0001

maci = open(0).read().split("\n\n")
ans = 0
for i, machine in enumerate(maci):
    l = [l.strip() for l in machine.split("\n") if l.strip()]

    vals: list[list[int]] = []
    for aline in l:
        coords = aline[aline.index(":") + 2 :].split(",")
        sep = "+" if "+" in coords[0] else "="
        x, y = [int(s[s.index(sep) + 1 :]) for s in coords]
        vals.append([x, y])

    coeff = vals[:2]
    b = vals[-1]
    b = [10000000000000 + x for x in b]
    sol = solve(numpy.transpose(coeff), b)
    ac, bc = map(float, [sol[0], sol[1]])
    # print(coeff, b)
    # print(sol)
    # print(int(bc), float(bc))
    if abs(ac - round(ac)) < epsilon and abs(bc - round(bc)) < epsilon:
        if ac <= 0 or ac >= 100 or bc <= 0 or bc >= 100:
            print(f"Too many presses: {ac} {bc}")
        tokens = round(ac) * 3 + round(bc)
        print(f"{i}: {sol} => Tokens: {tokens}, {ac},{bc}")
        ans += tokens
    # else:
    #     print(f"{i}: {sol}, {ac} vs {round(ac)} ; {bc} vs {round(bc)} => Invalid")
print(f"Ans: {ans}")

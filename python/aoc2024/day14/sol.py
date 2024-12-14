import re

w = 101
h = 103
mc = w // 2
mr = h // 2
part1 = False
l = open(0).readlines()
pat = r"[+-]?\d+"

lines = []
for s in l:
    px, py, vx, vy = [int(x) for x in re.findall(pat, s.strip())]
    lines.append((px, py, vx, vy))

bots = lines

bots = [((px + 100 * vx) % w, (py + 100 * vy) % h, vx, vy) for (px, py, vx, vy) in bots]
qc = {}
for b in bots:
    px, py, vx, vy = b
    if px == w // 2 or py == h // 2:
        continue
    qx = px > (w // 2)
    qy = py > (h // 2)
    if (qx, qy) not in qc:
        qc[(qx, qy)] = 0
    qc[(qx, qy)] += 1

ans = 1
for v in qc.values():
    ans = ans * v
print(f"Ans: { ans }")


# part 2
bots = lines
cit = 0
ans = 0
lv = float("inf")


def check_tree(formation) -> int:
    tl = bl = tr = br = 0
    for px, py, _, _ in formation:
        if px == mc or py == mr:
            continue
        if px < mc:
            if py < mr:
                tl += 1
            else:
                bl += 1
        else:
            if py > mr:
                br += 1
            else:
                tr += 1
    return tl * tr * bl * br


while True:
    nv = check_tree(bots)
    if nv < lv:
        # print(f"New min {nv} over {lv} at {cit}")
        lv = nv
        ans = cit
    bots = [((px + vx) % w, (py + vy) % h, vx, vy) for (px, py, vx, vy) in bots]
    cit += 1
    if cit % 1000000 == 0:
        print(f"AT: {cit} iterations")
    if cit > (h * w):
        break

print(f"Ans: {ans}")

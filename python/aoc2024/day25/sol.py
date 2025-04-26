combos = open(0).read().split("\n\n")

locks = []
keys = []

for combo in combos:
    rows = [r.strip() for r in combo.splitlines()]
    isLock = False
    if all(x == "#" for x in rows[0]): isLock = True
    if isLock:
        rows = rows[1:]
    else:
        rows = rows[:-1]
    heights = [0]*len(rows[0])
    for row in rows:
        for j, c in enumerate(row):
            heights[j] += 1 if c == "#" else 0
    if isLock:
        locks.append(heights)
    else:
        keys.append(heights)


ans = 0
for lock in locks:
    for key in keys:
        ans += all([(lh + kh) <= 5 for lh, kh in zip(lock, key)])
print(ans)

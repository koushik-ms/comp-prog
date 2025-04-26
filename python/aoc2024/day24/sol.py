from collections import deque
import re

ops = [ "AND", "OR", "XOR" ]
delims = [f" {x} " for x in ops + ["->"]]
pat = "|".join(map(re.escape, delims))

wvs, gas = open(0).read().split("\n\n")

values = {}
for wv in wvs.splitlines():
    w, v = wv.strip().split(": ")
    values[w.strip()] = int(v.strip())

gaq = deque([s.strip() for s in gas.splitlines()])

while gaq:
    stmt = gaq.popleft()
    w1, w2, w3 = re.split(pat, stmt)
    if w1 not in values or w2 not in values:
        gaq.append(stmt)
        continue
    op = stmt.split()[1]
    if op == "AND":
        values[w3] = values[w1] and values[w2]
    elif op == "OR":
        values[w3] = values[w1] or values[w2]
    else:
        values[w3] = int(values[w1] != values[w2])
i = 0
bs = ""
while True:
    key=f"z{i:02}"
    if key not in values:
        break
    bs = f"{values[key]}{bs}"
    i += 1
print("Part 1:", int(bs,2))

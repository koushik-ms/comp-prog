from functools import cache

initial_numbers = [int(x) for x in open(0).readlines()]
ITER=2000
BASE = 16777216
def evolve(x):
    s1 = (x ^ (x*64)) % BASE
    s2 = (s1 ^ (s1//32)) % BASE
    return (s2 ^ (s2*2048)) % BASE

prices = [[n] for n in initial_numbers]
for _ in range(ITER):
    for x in prices:
        x.append(evolve(x[-1]))
ans = sum(x[-1] for x in prices)
print("Part 1: ", ans)
# assert ans == 17612566393, "Expected: 17612566393 Actual: " + str(ans)

nl = [ [x%10 for x in pl] for pl in prices]
cp = [ [b-a for a,b in zip(pl, pl[1:])] for pl in nl]
# print(cp)

@cache
def binb(change_sequence, bi):
    sl = sp[bi]
    return nl[bi][sl.index(change_sequence) + 4] if change_sequence in sl else 0


sequences = set()
sp = []
for cl in cp:
    sl = [tuple(cl[n:n+4]) for n in range(len(cl)-4)]
    sp.append(sl)
    sequences.update(sl)
sqel = len(sequences)
print(sqel, len(sp[0]), len(cp[0]), cp[0][-1])
print((-2, 1, -1, 3) in sequences)
bananas = (0, None)
for i, change_sequence in enumerate(list(sequences)):
    print(f"Seq: {i} of {sqel} - {100.0*i/sqel}%")
    gf = [
        binb(change_sequence, bi)
        for bi in range(len(sp))
    ]
    bpl = sum( gf    )
    # if change_sequence == (-2, 1, -1, 3):
    #     print(f"BPL for (-2, 1, -1, 3) is {bpl} using {gf}")
    if bpl > bananas[0]:
        bananas = (bpl, change_sequence)
print(bananas)

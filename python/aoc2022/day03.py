from string import ascii_letters
puz = [x.strip() for x in open(0).readlines()]
p = 0
for rs in puz:
    c1, c2 = rs[:len(rs)//2], rs[len(rs)//2:]
    mi = set(c1).intersection(set(c2))
    p += 1 + ascii_letters.index(mi.pop())
print(p)

l2 = 0
ng = len(puz)//3
for i in range(ng):
    mi = set(puz[(i*3)]).intersection(set(puz[(i*3+1)])).intersection(set(puz[(i*3+2)]))
    # print(f'{i=}: {mi=}')
    l2 += 1 + ascii_letters.index(mi.pop())
print(l2)
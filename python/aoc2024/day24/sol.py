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
# print("Processing equations...")
# while gaq:
#     stmt = gaq.popleft()
#     w1, w2, w3 = re.split(pat, stmt)
#     if w1 not in values or w2 not in values:
#         gaq.append(stmt)
#         continue
#     op = stmt.split()[1]
#     if op == "AND":
#         values[w3] = values[w1] and values[w2]
#     elif op == "OR":
#         values[w3] = values[w1] or values[w2]
#     else:
#         values[w3] = int(values[w1] != values[w2])
# i = 0
# bs = ""
# while True:
#     key=f"z{i:02}"
#     if key not in values:
#         print(f"Stopping at {key}")
#         break
#     bs = f"{values[key]}{bs}"
#     i += 1
# print("Part 1:", int(bs,2))

rep = {}
reverse_rep = {}
for s in gas.splitlines():
    v1, op, v2, vo = s.strip().replace("->", " ").split()
    if vo in rep:
        print(f"Error: Duplicate for {vo}:\n\t {s} \n\t {rep[vo]}")
    # rep[vo] = (op, v1, v2)
    desc = (op, min(v1, v2), max(v1, v2))
    rep[vo] = desc
    reverse_rep[desc] = vo
print(rep['z45'])

def reprOf(bit):
    if bit[0] in "xy":
        return bit
    op, v1, v2 = rep[bit]
    return f"{op}({reprOf(v1)},{reprOf(v2)})"

def canonicalReprOf(bit):
    if bit[0] in "xy": return bit
    if bit[0] not in "cz": return ""
    sv = bit[1:]
    pv = int(bit[1:])
    prev_pv = pv - 1
    prev_sv = f"{prev_pv:02}"
    if bit[0] == "c":
        if pv <= 0: return ""
        if pv == 1: return "AND(x00,y00)"
        return f"OR(AND(x{prev_sv},y{prev_sv}),AND(XOR(x{prev_sv},y{prev_sv}),{canonicalReprOf(f'c{prev_sv}')}))"
    if pv == 0:
        return "XOR(x00,y00)"
    return f"XOR(XOR(x{sv},y{sv}),{canonicalReprOf(f'c{sv}')})"

lab = {}
print(rep['wqc'], rep['qtf'])
for i in range(45):
    xn = f"x{i:02}"
    yn = f"y{i:02}"
    zn = f"z{i:02}"
    cn = f"c{i:02}"
    cnp1 = f"c{(i+1):02}"
    ln = f"l{i:02}"
    an = f"a{i:02}"
    bn = f"b{i:02}"
    if i == 0:
        zc = ('XOR', xn, yn)
        cnp1_rep = ('AND', xn, yn)
        [print("Error missing {} for {}".format(var, i)) for var in [zc, cnp1_rep] if var not in reverse_rep]
        if zc in reverse_rep:
            lab['z00'] = reverse_rep[zc]
        if cnp1_rep in reverse_rep:
            lab['c01'] = reverse_rep[cnp1_rep]
        continue
    if cn not in lab: print("Error: Missing {} in lab".format(cn))
    cn_m = lab[cn]
    print(f"{i}: {xn} {yn} {cn_m}")
    ln_rep = ('XOR', xn, yn)
    if ln_rep not in reverse_rep: print(f"Error: {i} missing {ln_rep} in equations!")
    ln_m = reverse_rep[ln_rep]
    print(f"\t{ln} = {ln_m}")
    an_rep = ('AND', xn, yn)
    if an_rep not in reverse_rep: print(f"Error: {i} missing an_rep: {an_rep} in equations!")
    an_m = reverse_rep[an_rep]
    print(f"\t{an} = {an_m}")
    bn_rep = ('AND', min(ln_m, cn_m), max(ln_m, cn_m))
    if bn_rep not in reverse_rep: print(f"Error: {i} missing bn_rep: {bn_rep} in equations!")
    bn_m = reverse_rep[bn_rep]
    print(f"\t{bn} = {bn_m}")
    cnp1_rep = ('OR', min(an_m, bn_m), max(an_m, bn_m))
    if cnp1_rep not in reverse_rep: print(f"Error: {i} missing cnp1_rep: {cnp1_rep} in equations!")
    cnp1_m = reverse_rep[cnp1_rep]
    print(f"\t{cnp1} = {cnp1_m}")
    lab[cnp1] = cnp1_m
    zn_rep = ('XOR', min(ln_m, cn_m), max(ln_m, cn_m))
    if zn_rep not in reverse_rep: print(f"Error: Missing {zn} rep {zn_rep} in equations!")
    zn_m = reverse_rep[zn_rep]
    print(f"\t{zn} = {zn_m}")
    lab[zn] = reverse_rep[zn_rep]
print(lab)
sw = ['vss', 'z14', 'hjf', 'kdh', 'kpp', 'z31', 'sgj', 'z35']
print(",".join(sorted(sw)))

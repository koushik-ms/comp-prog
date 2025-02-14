regvals, progspec = [x.strip() for x in open(0).read().split("\n\n")]

program = [int(x) for x in progspec.split(":")[-1].strip().split(",")]
registers = {}
ip = 0
res = []
for r in regvals.splitlines():
    prefname, value = r.strip().split(":")
    registers[prefname.strip()[-1]] = int(value.strip())


def get_combo_val(val):
    if val < 4:
        return val
    if val < 5:
        return registers["A"]
    if val < 6:
        return registers["B"]
    if val < 7:
        return registers["C"]
    raise Exception("Invalid val: {}".format(val))


def adv(val):
    val = get_combo_val(val)
    registers["A"] >>= val


def bxl(val):
    registers["B"] ^= val


def bst(val):
    registers["B"] = get_combo_val(val) % 8


def jnz(val):
    global ip
    if 0 != registers["A"]:
        ip = val


def bxc(val):
    registers["B"] ^= registers["C"]


def out(val):
    global res
    val = get_combo_val(val) % 8
    res.append(val)


def bdv(val):
    registers["B"] = registers["A"] >> get_combo_val(val)


def cdv(val):
    registers["C"] = registers["A"] >> get_combo_val(val)


operations = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def functif(aprev, goal):
    candies = []
    for guess in range(7):
        ag = aprev * 8 + guess
        B = ag % 8
        # print(f"{guess} [A={ag} -> B={B} -> ", end="")
        B ^= 5
        C = ag // (2**B)
        ag //= 8
        # print(f"{B}, C={C}, A -> {ag} ", end= "")
        B ^= C
        B ^= 6
        B %= 8
        # print(f"out -> {B} [C = {C} A = {ag}]")
        if B == goal:
            candies.append(guess)
    return candies


while ip < len(program):
    op = operations[program[ip]]
    val = program[ip + 1]
    ip += 2
    op(val)
print(f"Part 1: {res}")

aprevs = [0]
for goal in reversed(program):
    nap = set()
    for aprev in aprevs:
        nap.update([aprev * 8 + candy for candy in functif(aprev, goal)])
    # print(f"{aprevs} -> {nap}")
    aprevs = list(nap)
print("Part 2:", min(aprevs))

puz = open(0).readlines()

def wol1(they, you):
    you_index = "XYZ".index(you)
    return (1 + you_index) + 3 * ((1 + you_index - "ABC".index(they)) % 3)

def wol2(they, result):
    you_index = ("ABC".index(they) + "XYZ".index(result) - 1) % 3
    return 1 + you_index + "XYZ".index(result)*3

level1, level2 = [sum(f(*l.split()) for l in puz) for f in [wol1, wol2]]
assert level1 == 13446, f'{level1=}'
assert level2 == 13509, f'{level2=}'
print(level1)
print(level2)

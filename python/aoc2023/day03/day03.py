from .p01 import al

NUMBERS = "0123456789"


def get_nums(mat):
    h = len(mat)
    ans = []
    for i, row in enumerate(mat):
        l = len(row)
        j = 0
        while j < l:
            if row[j].isnumeric():
                eat_number = False
                number = 0
                if j > 0:
                    if (
                        (row[j - 1] != ".")
                        or (i > 0 and mat[i - 1][j - 1] != ".")
                        or (i < (h - 1) and mat[i + 1][j - 1] != ".")
                    ):
                        eat_number = True
                while j < l and row[j].isnumeric():
                    if (not eat_number) and i > 0 and mat[i - 1][j] != ".":
                        eat_number = True
                    if (not eat_number) and i < (h - 1) and mat[i + 1][j] != ".":
                        eat_number = True
                    number = number * 10 + (ord(row[j]) - ord("0"))
                    j += 1
                if j < l:
                    if (
                        (row[j] != ".")
                        or (i > 0 and mat[i - 1][j] != ".")
                        or (i < (h - 1) and mat[i + 1][j] != ".")
                    ):
                        eat_number = True
                if eat_number:
                    ans.append(number)
                # else:
                # print(f"Not a part number: {number}")
            j += 1
    return sum(ans)


def get_gears(mat):
    h = len(mat)
    gears = []
    for i, row in enumerate(mat):
        l = len(row)
        j = 0
        while j < l:
            if row[j].isnumeric():
                eat_number = False
                number = 0
                gear_loc = None
                if j > 0:
                    if (
                        (row[j - 1] != ".")
                        or (i > 0 and mat[i - 1][j - 1] != ".")
                        or (i < (h - 1) and mat[i + 1][j - 1] != ".")
                    ):
                        eat_number = True
                    if row[j - 1] == "*":
                        gear_loc = (i, j - 1)
                    if i > 0 and mat[i - 1][j - 1] == "*":
                        gear_loc = (i - 1, j - 1)
                    if i < (h - 1) and mat[i + 1][j - 1] == "*":
                        gear_loc = (i + 1, j - 1)
                while j < l and row[j].isnumeric():
                    if (not eat_number) and i > 0 and mat[i - 1][j] != ".":
                        eat_number = True
                    if (not eat_number) and i < (h - 1) and mat[i + 1][j] != ".":
                        eat_number = True
                    if i > 0 and mat[i - 1][j] == "*":
                        gear_loc = (i - 1, j)
                    if i < (h - 1) and mat[i + 1][j] == "*":
                        gear_loc = (i + 1, j)
                    number = number * 10 + (ord(row[j]) - ord("0"))
                    j += 1
                if j < l:
                    if (
                        (row[j] != ".")
                        or (i > 0 and mat[i - 1][j] != ".")
                        or (i < (h - 1) and mat[i + 1][j] != ".")
                    ):
                        eat_number = True
                    if row[j] == "*":
                        gear_loc = (i, j)
                    if i > 0 and mat[i - 1][j] == "*":
                        gear_loc = (i - 1, j)
                    if i < (h - 1) and mat[i + 1][j] == "*":
                        gear_loc = (i + 1, j)
                if eat_number and gear_loc:
                    print(f"Adding: {(gear_loc, number)}")
                    gears.append((gear_loc, number))
                else:
                    print(f"Not a gear: {number}")
            j += 1
    ans = 0
    gears.sort()
    for i in range(len(gears)-1):
        if gears[i][0] == gears[i+1][0]:
            ans += gears[i][1] * gears[i+1][1]
    return ans


def part1():
    print("AoC 2023: 3.1")
    ts = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split(
        "\n"
    )
    print(get_nums(ts))
    print(get_nums(al))


def part2():
    print("AoC 2023: 3.2")
    ts = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split(
        "\n"
    )
    print(get_gears(ts))
    print(get_gears(al))


if __name__ == "__main__":
    part1()
    part2()

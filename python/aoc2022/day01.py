puz = open(0).read().split("\n\n")

calories = [sum(map(int, d.strip().split("\n"))) for d in puz]
print(max(calories))
print(sum(sorted(calories)[-3:]))
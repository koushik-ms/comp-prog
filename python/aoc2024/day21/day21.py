from .sol import solve

print("AoC 2024: 21")
tl = [r.strip() for r in open("day21/21.in").readlines()]
part1, part2 = solve(tl)
assert part1 == 126384, f"Expected: 126384 vs actual {part1}"
assert part2 == 154115708116294, f"Expected: 154115708116294 vs Actual: {part2}"
al = [r.strip() for r in open("day21/21.txt").readlines()]
part1, part2 = solve(al)
print("Part 1:", part1)
print("Part 2:", part2)
assert 128962 == part1, f"Expected: 128962 vs {part1}"
assert 159684145150108 == part2, f"Expected: 159684145150108 vs {part2}"

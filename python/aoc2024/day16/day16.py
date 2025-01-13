from .sol import solve

print("AoC 2024: 16.1")
tl = [list(r.strip()) for r in open("day16/16.ex").readlines()]
part1, part2 = solve(tl)
assert part1 == 7036, f"Expected: 7036 vs actual {part1}"
assert part2 == 45, f"Expected: 45 vs Actual: {part2}"
tl = [list(r.strip()) for r in open("day16/16.in").readlines()]
part1, part2 = solve(tl)
assert part1 == 11048, f"Expected: 11048 vs actual {part1}"
assert part2 == 64, f"Expected: 64 vs Actual: {part2}"
al = [list(r.strip()) for r in open("day16/16.txt").readlines()]
part1, part2 = solve(al)
print("Part 1:", part1)
print("Part 2:", part2)
assert 105508 == part1, f"Expected: 105508 vs {part1}"
assert 548 == part2, f"Expected: 548 vs {part2}"

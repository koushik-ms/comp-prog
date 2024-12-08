#!/usr/bin/env python


from typing import Callable


def solve(lines: list[str], part2: bool = False) -> int:
    antenna_points: dict[str, list[tuple[int, int]]] = {}
    grid = [list(r.strip()) for r in lines]
    h = len(grid)
    w = len(grid[0])
    inb: Callable[[int, int], bool] = lambda r, c: (0 <= r < h) and (0 <= c < w)
    for r in range(h):
        for c in range(w):
            if grid[r][c] != ".":
                loclist = antenna_points.get(grid[r][c], [])
                loclist.append((r, c))
                antenna_points[grid[r][c]] = loclist

    antinodes: set[tuple[int, int]] = set()
    for ac in antenna_points.keys():
        loclist = antenna_points[ac]
        size = len(loclist)
        for i in range(size):
            x1, y1 = loclist[i]
            if part2:
                antinodes.add((x1, y1))
            for j in range(i + 1, size):
                x2, y2 = loclist[j]
                dx = x2 - x1
                dy = y2 - y1
                n1x, n1y = x1 - dx, y1 - dy
                while inb(n1x, n1y):
                    antinodes.add((n1x, n1y))
                    if not part2:
                        break
                    n1x, n1y = n1x - dx, n1y - dy
                n2x, n2y = x2 + dx, y2 + dy
                while inb(n2x, n2y):
                    antinodes.add((n2x, n2y))
                    if not part2:
                        break
                    n2x, n2y = n2x + dx, n2y + dy

    return len(antinodes)


if __name__ == "__main__":
    lines = open(0).readlines()
    for part2 in [False, True]:
        print(solve(lines, part2))

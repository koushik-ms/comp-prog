
from collections import deque
from .p01 import al

tl = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
tl=al

mat = [[c for c in row] for row in tl]
h = len(mat)
w = len(mat[0]) if h else 0


def fill(sr, sc, limit, part1=True):
    Q = deque([(sr, sc, int(0))])
    visited = set()
    ans = 0
    i = 0
    while Q:
        i += 1
        r, c, d = Q.popleft()
        if i%10**6 == 0:
            print(i, d, ans)
        if part1 and not (0<=r<h and 0<=c<w and mat[r][c] in ".S"):
            continue
        if not part1 and not mat[r%h][c%w] in ".S":
            continue
        if (r,c) in visited:
            continue
        visited.add((r,c))
        if d>limit:
            continue
        if d<=limit and (limit-d)%2 == 0:
            ans += 1
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            Q.append((r+dr, c+dc, d+1))
    return ans

sr, sc = next((r,c) for r, row in enumerate(tl) for c, ch in enumerate(row) if ch == "S")
print("AoC 2023: Day 21.1")
# print(sr,sc)
print(fill(sr, sc, limit=64, part1=True))

print("AoC 2023: Day 21.2")
L = 26501365

# for pl in [300, 301]:
#     print("step count:", pl)
#     print("top-left :", fill(0, 0, pl))
#     print("mid-left :", fill(sr, 0, pl))
#     print("bot-left :", fill(h-1, 0, pl))
#     print("top-mid  :", fill(0,sc,pl))
#     print("center:  :", fill(sr, sc, pl))
#     print("bot-mid  :", fill(h-1, sc, pl))
#     print("top-right:", fill(0, w-1, pl))
#     print("mid-right:", fill(sr, w-1, pl))
#     print("bot-right:", fill(h-1, w-1, pl))

# everything below assumes mat is odd size and square
even_cov, odd_cov = [fill(sr, 0, pl) for pl in [2*h, 2*h+1]]
# print(f"{even_cov=}, {odd_cov=}")

# part 2 cannot be brute-forced. test input and real input are both
# square matrices with odd number of rows/cols. However, the real
# input has entire permimeter + center row/col "free" (no rocks)
# So below reasoning uses real input as basis.

# assume L is such that if we keep walking straight (up/ down/ left/ right)
# we reach a tile boundary at the end of L steps, where 1 tile = 1 instance of mat
# This way we can cover a diamond shaped area ◆ with some tiles falling fully
# within and some falling on the border. The diamond extends, say gw tiles on each
# side from the center square. To check this assumption, test if L-h//2 is a 
# multiple of h and find gw

gw = (L-h//2)//h

# gw = 202300 !! easter egg !! at christmas time!

# now after some grid plotting we know that we will have a gwxgw set of tiles
# fully reachable interspersed with a (gw-1)*(gw-1) set also fully reachable.
# Since L is odd, tiles in outer grid will be reachable with odd steps left
# since h//2+1 + 2k*h steps will be required to enter it from sr, sc. 
# Similarly, inner_grid tiles will be reachable with even steps left.
outer_grid = gw*gw
inner_grid = (gw-1)*(gw-1)
# print(f'{h=}, {w=}, {L=}')
# print("Repeat :", gw, "times!")
# print(f"{outer_grid=} , {inner_grid=}")

outer_points = odd_cov if gw % 2 == 0 else even_cov
inner_points = even_cov if gw % 2 == 0 else odd_cov

outer_points *= outer_grid
inner_points *= inner_grid
# print(f'{outer_points=}, {inner_points=}')

# At the four corners of the diamond, the fastest way to reach them is by
# walking straight and thus enter then with h-1 steps left.
top = fill(h-1, sc, h-1)
right = fill(sr, 0, h-1)
bottom = fill(0, sc, h-1)
left = fill(sr, w-1, h-1)
# print(f'{top=}, {right=}, {bottom=}, {left=}')

# Along the border of the diamond, there are partially reachable tiles,
# some with small cut through them, and others with large cut through them.
# These are resp the boundary tiles of the outer and inner grid and thus
# have h//2-1(even) and 3h//2-1(odd) steps left when entered and those on 
# each bordered can be reached quickest by the nearst corner from center.
sc_tr = fill(h-1, 0, h//2-1)
lc_tr = fill(h-1, 0, h+h//2-1)
sc_br = fill(0, 0, h//2-1)
lc_br = fill(0, 0, h+h//2-1)
sc_bl = fill(0, w-1, h//2-1)
lc_bl = fill(0, w-1, h+h//2-1)
sc_tl = fill(h-1, w-1, h//2-1)
lc_tl = fill(h-1, w-1, h+h//2-1)
# print(f'{sc_tr=}, {sc_br=}, {sc_bl=}, {sc_tl=}')
# print(f'{lc_tr=}, {lc_br=}, {lc_bl=}, {lc_tl=}')

# In all the obove cases, there are other ways to reach the tiles but
# reaching through the fastest way will give us the most garden blocks
# reached and thus supersede any other paths for the same tile.

# Finally we add all the blocks reached in all the tiles
ans = (
    outer_points + inner_points +
    top + right + bottom + left +
    gw * (sc_tr + sc_br + sc_bl + sc_tl) +
    (gw-1) * (lc_tr + lc_br + lc_bl + lc_tl) 
)
print(ans)

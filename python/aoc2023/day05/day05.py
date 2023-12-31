from .p01 import al

flat_map = lambda f, xs: [y for x in xs for y in f(x)]

def part1():
    print("AoC 2023: 5.1")
    ss = """45 77 23
81 45 19
68 64 13""".split("\n")
    fn = get_mapper(ss)
    print(fn(74)) # 78
    tl = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    print(map_through(tl))
    print(map_through(al))

def part2():
    print("AoC 2023: 5.2")
    tl = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    print(map_pairs(tl))
    print(map_pairs(al))

def map_pairs(tl):
    ss, ts = tl.split("\n\n", maxsplit=1)
    sl = [ int(v) for v in ss.split(": ")[-1].strip().split()]
    ans = None
    for i in range(0, len(sl), 2):
        v = [(sl[i], sl[i+1])]
        for m in mappers(ts, tfgen=get_interval_mapper):
            v = flat_map(m, v)
        minv = min(v)
        if ans is None or ans > minv[0]:
            ans = minv[0]
    return ans

def map_through(tl):
    ss, ts = tl.split("\n\n", maxsplit=1)
    sl = [ int(v) for v in ss.split(": ")[-1].strip().split()]
    ll = []
    for v in sl:
        for m in mappers(ts):
            v = m(v)
        ll.append(v)
    return min(ll)

def get_mapper(ss):
    def trans(lt, s):
        for ds, ss, w in lt:
            if s >= ss and s < ss+w:
                return ds + (s-ss)
        return s
    gf = [[int(x) for x in v.split()] for v in ss]
    return lambda x: trans(gf,x)

def get_interval_mapper(ss):
    def trans(lt, si):
        sis, siw = si
        ans = []
        # assume lt is sorted by ss (start of source range)
        for ds, ss, w in lt:
            if siw <= 0:
                break
            if sis < ss:
                tiw = min(siw, ss-sis)
                ans.append((sis, tiw))
                siw -= tiw
                sis += tiw
            if siw > 0 and (ss+w) > sis:
                tiw = min(siw, ss+w-sis)
                ans.append((ds+(sis-ss), tiw))
                siw -= tiw
                sis += tiw
        if siw > 0:
            ans.append((sis, siw))
        return ans
    il = [tuple(int(x) for x in v.split()) for v in ss]
    il.sort(key=lambda e: e[1])
    return lambda x: trans(il, x)

def mappers(tl, tfgen = get_mapper):
    sections = tl.split("\n\n")
    return [tfgen(section.split("\n")[1:]) for section in sections]

if __name__ == "__main__":
    part1()
    part2()

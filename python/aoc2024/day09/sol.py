def solve(fs: str, part2: bool = False) -> int:
    rep: list[tuple[int, int]] = []
    id = 0
    l = list(fs.strip())
    while l:
        sz = int(l.pop(0))
        pad = int(l.pop(0)) if l else 0
        rep.append((id, sz))
        if pad:
            rep.append((-1, pad))
        id += 1

    rerep: list[tuple[int, int]] = []
    while rep:
        i, e = rep.pop()
        if i == -1:
            rerep.append((i, e))
            continue
        for k, (ji, je) in enumerate(rep):
            if not part2:
                if ji == -1:
                    if e <= je:
                        sl = [(i, e)]
                        if e < je:
                            sl += [(ji, je - e)]
                        rep = rep[:k] + sl + rep[k + 1 :]
                    else:
                        sl = [(i, je)]
                        e -= je
                        rep = rep[:k] + sl + rep[k + 1 :] + [(i, e)]
                    e = 0
                    break
            if part2:
                if ji == -1 and je >= e:
                    je -= e
                    sl = [(i, e)]
                    if je > 0:
                        sl.append((ji, je))
                    rep = rep[:k] + sl + rep[k + 1 :]
                    rerep.append((-1, e))
                    e = 0
                    break
        if e:
            rerep.append((i, e))

    pos = 0
    ans = 0
    for j in range(len(rerep)):
        i, e = rerep[len(rerep) - j - 1]
        while e:
            ans += pos * i if i != -1 else 0
            pos += 1
            e -= 1
    return ans


if __name__ == "__main__":
    l = open(0).read()
    for part2 in [False, True]:
        ans = solve(l, part2)
        print(ans)

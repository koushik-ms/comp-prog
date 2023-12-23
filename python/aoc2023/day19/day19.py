from functools import reduce
from .p01 import al

def props(s):
    m = [st for st in s.strip("{} \t\r\n").split(",") ]
    ans = {}
    for p in m:
        k, v = p.split("=")
        ans[k] = int(v)
    return ans


def wf(s):
    name, steps = s.split("{")
    spec = []
    for step in steps.strip("{} ").split(","):
        if ":" in step:
            cond, target = step.split(":")
        else:
            cond, target = "True", step
        spec.append({"cond": cond, "target": target})
    return name, spec


def get_target(part, job):
    (x,m,a,s) = (part[c] for c in "xmas")
    for step in job:
        # print(f"==> Evaluating {step['cond']=} for {step['target']=}")
        if eval(step["cond"]):
            return step['target']
    return "A"

def result(part, workflows):
    """ Return rating number of part based on workflows 
    Given a part, find out if the part will be accepted or rejected
    as result of running all workflows on part starting from `in`
    if part is accepted, rating number is sum of all its props.
    if part is rejected, rating number is 0.
    """
    sw = "in"
    res = None
    while res is None:
        # print(f"{part=}, {res=}, {sw=}")
        tw = get_target(part, workflows[sw])
        if tw == "A":
            res = sum(part.values())
        elif tw == "R":
            res = 0
        # print(f"        => {tw=} {res=}")
        sw = tw
    return res


def rating_numbers(wfs, pspecs):
    # print(f"{wfs=}, {pspecs=}")
    workflows = {}
    res = []
    for job in wfs.splitlines():
        name, spec = wf(job)
        workflows[name] = spec
    for ps in pspecs.splitlines():
        part = props(ps)
        res.append(result(part, workflows))
    return sum(res)

def combis(wfs, pspecs):
    poss = lambda d: reduce(lambda x,y: x*y, [r-l+1 for l, r in d.values()])
    res = 0
    # for job in wfs.splitlines():
    #     name, spec = wf(job)
    #     workflows[name] = spec
    workflows = {name: spec for name, spec in map(wf, wfs.splitlines())}
    pr = {k:(1,4000) for k in "xmas"}
    pp: list[tuple[str,dict[str,tuple[int,int]]]] = [("in", pr)]
    while pp:
        cw, cr = pp.pop(0)
        tr = []
        # print(f"{cw=} {res=}")
        if cw in "AR":
            res += poss(cr) if ( cw == "A" ) else 0
            # print(f"  => {cr} => {res=}")
            continue
        for step in workflows[cw]:
            ranges_ok = [r[0] <= r[1] for r in cr.values()]
            # print(f"  => {cr=}: {ranges_ok=}")
            if not all(ranges_ok):
                # print(f"    => skipping")
                break
            cond = step["cond"]
            target = step["target"]
            # print(f"    >> {step=}: {cond=}, {target=}")
            if cond == "True":
                tr.append((target, cr))
                # print(f"    >> add ({target=}, {cr=})")
                break
            el = cond[0]
            op = cond[1]
            ip = int(cond[2:])
            nr = {k:v for k,v in cr.items()}
            if op == "<" and cr[el][0] < ip:
                rext = min(ip-1, nr[el][1])
                nr[el] = (nr[el][0], rext)
                tr.append((target, nr))
                # print(f"    >> add ({target=}, {nr=})")
                cr[el] = (ip, cr[el][1]) # which could be invalid
            if op == ">" and cr[el][1] > ip:
                lext = max(ip+1, nr[el][0])
                nr[el] = (lext, nr[el][1])
                tr.append((target, nr))
                # print(f"    >> add ({target=}, {nr=})")
                cr[el] = (cr[el][0], ip) # which could be invalid
        # print(f"  =>> {tr=}")
        pp.extend(tr)

    return res

def part1():
    print("AoC 2023: 19.1")
    ts = "{x=787,m=2655,a=1222,s=2876}"
    print(props(ts))
    ts = "px{a<2006:qkq,m>2090:A,rfg}"
    print(wf(ts))
    tl = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}""".split("\n\n")
    print(rating_numbers(*tl))
    print(rating_numbers(*al))


def part2():
    print("AoC 2023: 19.2")
    tl = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}""".split("\n\n")
    pt = combis(*tl)
    print(pt)
    assert pt == 167409079868000
    pa = combis(*al)
    print(pa)
    assert pa == 122112157518711


if __name__ == "__main__":
    part1()
    part2()
 

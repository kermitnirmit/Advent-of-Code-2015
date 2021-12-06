import parse
a = {"children": 3,
     "cats": 7,
     "samoyeds": 2,
     "pomeranians": 3,
     "akitas": 0,
     "vizslas": 0,
     "goldfish": 5,
     "trees": 3,
     "cars": 2,
     "perfumes": 1}

def solve(part_two=False):
    f = [x for x in open("input.txt").read().strip().split("\n")]
    for k, v in a.items():
        # if v != 0:
        if k in ["cats", "trees"] and part_two:
            shortList = []
            for l in f:
                if k in l:
                    good = False
                    # there are cats or trees somewhere
                    parsed = list(parse.parse("Sue {:d}: {}: {:d}, {}: {:d}, {}: {:d}", l))
                    for index, parsedv in enumerate(parsed):
                        if parsedv == k:
                            if parsed[index + 1] > v:
                                good = True
                    if good:
                        shortList.append(l)
                else:
                    shortList.append(l)
            f = shortList
        elif k in ["pomeranians", "goldfish"] and part_two:
            shortList = []
            for l in f:
                if k in l:
                    good = False
                    parsed = list(parse.parse("Sue {:d}: {}: {:d}, {}: {:d}, {}: {:d}", l))
                    for index, parsedv in enumerate(parsed):
                        if parsedv == k:
                            if parsed[index + 1] < v:
                                good = True
                    if good:
                        shortList.append(l)
                else:
                    shortList.append(l)
            f = shortList
        else:
            f = list(filter(lambda x: f"{k}: {v}" in x or k not in x, f))
        # print(len(f))
    if(len(f)) == 1:
        print(f)


solve()
solve(True)

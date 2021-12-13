from collections import defaultdict
from itertools import permutations
import parse
f = open("input.txt").read().strip().split("\n")
pairing_map = defaultdict(dict)


def solve(include_you = False):
    for l in f:
        name, g, num, partner = parse.parse("{} would {} {:d} happiness units by sitting next to {}.", l).fixed
        sign = 1 if g == "gain" else -1
        pairing_map[name][partner] = num * sign
        if include_you:
            pairing_map[name]["you"] = 0
    names = list(pairing_map.keys())
    if include_you:
        for name in names:
            pairing_map["you"][name] = 0
    a = -100000000
    for p in permutations( list(pairing_map.keys())):
        p = list(p)
        score = 0
        for q,w in zip(p, p[1:] + [p[0]]):
            score += pairing_map[q][w]
            score += pairing_map[w][q]
        a = max(score, a)
    return a


print(solve(False))
print(solve(True))

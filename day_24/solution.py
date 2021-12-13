from collections import defaultdict
from itertools import combinations

f = [int(x) for x in open("input.txt").read().strip().split("\n")]


def solve(parts=4):
    f = [int(x) for x in open("input.txt").read().strip().split("\n")]
    target = sum(f) // parts
    d = defaultdict(list)
    i = 1
    while True:
        found = False
        for comb in combinations(f, i):
            if sum(comb) == target:
                d[i].append(comb)
                found = True
        if found:
            break
        else:
            i += 1
    minProd = 100000000000000
    for a in d[i]:
        prod = 1
        for z in list(a):
            prod *= z
        minProd = min(prod, minProd)
    return minProd


print(solve(3))
print(solve(4))

from collections import defaultdict
from itertools import  combinations
containers = [int(x) for x in open("input.txt").read().strip().split("\n")]
c = 0
d = defaultdict(int)
for i in range(1 << len(containers)):
    count = 0
    qwer = 0
    for idx, val in enumerate(containers):
        if (i & 1<<idx) > 0:
            qwer += val
            count += 1
    if qwer == 150:
        c += 1
        d[count] += 1
print(c)
print(d[min(d.keys())])


c = 0
d = defaultdict(int)
for i in range(len(containers)):
    for comb in combinations(containers, i):
        if sum(comb) == 150:
            c += 1
            d[i] += 1
print(c)
print(d[min(d.keys())])




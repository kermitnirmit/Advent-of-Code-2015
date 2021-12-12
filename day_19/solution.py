# you can do one replacement on the medicine molecule?
import re
from collections import defaultdict
f = [x for x in open("input.txt").read().strip().split("\n")]
# f = [x for x in open("small.txt").read().strip().split("\n")]

orig = f[-1]

conversions = f[:-2]

d = defaultdict(list)

for line in conversions:
    left, right = line.split(" => ")
    d[left].append(right)

visited = set()

def find_all_one_away(str, level, target=None):
    retList = []
    for k,v in d.items():
        for rep in v:
            a = re.finditer(k, str)
            for i in a:
                newStr = str[:i.start(0)] + rep + str[i.end(0):]
                if newStr not in visited:
                    if target is not None and target == newStr:
                        print("found it!", level + 1)
                        break
                    visited.add(newStr)
                    retList.append((newStr, level + 1))
    return retList
print(len(find_all_one_away(orig, 0)))

# https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju/
print(len(list(filter(lambda x: x.isupper(), orig))) - 2*orig.count("Rn") - 2*orig.count("Y") - 1)
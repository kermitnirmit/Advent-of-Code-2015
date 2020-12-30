from collections import defaultdict
from utils import neighbors_2d
f = open("input.txt").read().strip().split("\n")


old = defaultdict(int)
for i in range(len(f)):
    for j in range(len(f[i])):
        old[(i,j)] = 1 * f[i][j] == "#"


def find_neighbors(i,j, old):
    ret = 0
    for dx, dy in neighbors_2d:
        newx, newy = i + dx, j + dy
        if 0<= newx < 100 and 0<= newy < 100:
            ret += old[(newx, newy)]
    return ret
# comment next line to run part 1
old[(0,0)] = old[(0,99)] = old[(99,0)] = old[(99,99)] = 1

for _ in range(100):
    new_day = defaultdict(int)
    for i in range(100):
        for j in range(100):
            n = find_neighbors(i, j, old)
            if old[(i,j)] == 1:
                if 2<=n<=3:
                    new_day[(i,j)] = 1
                else:
                    new_day[(i,j)] = 0
            else:
                if n == 3:
                    new_day[(i,j)] = 1
                else:
                    new_day[(i,j)] = 0
    old = new_day
    # comment next line to run part 1
    old[(0,0)] = old[(0,99)] = old[(99,0)] = old[(99,99)] = 1




print(sum(old.values()))
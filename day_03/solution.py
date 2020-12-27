from collections import defaultdict
dirs = [(0,1), (1,0), (0, -1), (-1, 0)]
dir_mapping = dict(zip(list("^>v<"), dirs))
presents = defaultdict(int)

f = list(open('input.txt').read().strip())
# f = list("^v^v^v^v^v")

pos = [0,0]
presents[(0,0)] = 1
for a in f:
    dx, dy = dir_mapping[a]
    pos[0] += dx
    pos[1] += dy
    # print(pos)
    presents[tuple(pos)] += 1
    # print(presents)
count = 0
for k, v in presents.items():
    if v > 0:
        count += 1
print(count)

presents = defaultdict(int)
presents[(0,0)] = 2
santaPos = [0,0]
roboPos = [0,0]

def move_santa(move, qpos):
    dx, dy = dir_mapping[move]
    qpos[0] += dx
    qpos[1] += dy
    # print(pos)
    presents[tuple(qpos)] += 1
    return qpos



for i in range(len(f)):
    if i % 2 == 0:
        santaPos = move_santa(f[i], santaPos)
    else:
        roboPos = move_santa(f[i], roboPos)

count = 0
for k, v in presents.items():
    if v > 0:
        count += 1
print(count)

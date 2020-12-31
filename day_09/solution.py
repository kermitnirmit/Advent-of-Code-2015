from itertools import permutations
f = open("input.txt").read().strip().split("\n")


adjacency_matrix = {}
# nodes to a dictionary with edge to cost pair?

for line in f:
    places, cost = line.split(" = ")
    cost = int(cost)
    a, b = places.split(" to ")
    if a in adjacency_matrix:
        adjacency_matrix[a][b] = cost
    else:
        adjacency_matrix[a] = dict({b: cost})
    if b in adjacency_matrix:
        adjacency_matrix[b][a] = cost
    else:
        adjacency_matrix[b] = dict({a: cost})

ones_to_check = set()
for p in permutations(adjacency_matrix.keys()):
    if p[::-1] not in ones_to_check:
        ones_to_check.add(p)

mindist = 100000000000000
maxdist = -10
for one in ones_to_check:
    qwer = list(one)
    dist = 0
    for src, dest in zip(qwer, qwer[1:]):
        dist += adjacency_matrix[src][dest]
    mindist = min(mindist, dist)
    maxdist = max(maxdist, dist)

print(f"part 1 answer: {mindist}")
print(f"part 2 answer: {maxdist}")


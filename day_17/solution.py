from collections import Counter
containers = [int(x) for x in open("input.txt").read().strip().split("\n")]
containers = [20, 15, 10, 5, 5]
countainer_counts = Counter(containers)
containers = set(containers)
combinations = [0] * 26

for i in range(1, 26):
    for size in containers:
        # print("checking size", size)
        if i - size == 0 or combinations[i - size] != 0:
            if i == 10:
                print("incrementing something for 10")
                print(i, size, combinations[i], combinations[i - size], countainer_counts[size])
            combinations[i] += (combinations[i - size] + countainer_counts[size])
print(combinations[10])
# print(combinations[-1])


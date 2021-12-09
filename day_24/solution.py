f = [int(x) for x in open("input.txt").read().strip().split("\n")]


third = sum(f) // 3
print(third)

f = sorted(f)[::-1]
retList = []

# printSubsequences(f, 0, [])

# print(len(retList))

print(f)
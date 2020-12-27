from collections import Counter
f = list(open('input.txt').read().strip())

# print(f)

c = Counter(f)

print(c["("] - c[")"])


floor = 0
for i, a in enumerate(f):
    if a == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(i + 1)
        break
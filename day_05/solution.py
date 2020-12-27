from collections import Counter, defaultdict
f = open('input.txt').read().strip().split("\n")
# f = ["qjhvhtzxzqqjkmpb", "xxyxx"]

vowels = "aeiou"


banned_strings = ["ab", "cd", "pq", "xy"]

def process_string(x):
    if any(bs in x for bs in banned_strings):
        return False
    c = Counter(x)
    q = 0
    for v in vowels:
        q += c[v]
    if q < 3:
        return False
    return any(a == b for a,b in zip(x, x[1:]))

def process_string_2(x):
    qwer = defaultdict(int)
    for a,b in zip(x, x[1:]):
        qwer[(a,b)] += 1
    if all(a != b and val < 2 or a == b and val < 3 for (a,b), val in qwer.items()):
        return False
    return any(a == b for a,b in zip(x, x[2:]))

nice_strings = [x for x in f if process_string(x)]

print(len(nice_strings))

# nice_strings = [x for x in f if process_string_2(x)]

# print(nice_strings)


# print(zip("12345", "2345"))

# for i, (a,b) in enumerate(zip("12345", "2345")):
#     print(i,a,b)
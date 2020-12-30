from collections import Counter, defaultdict
f = open('input.txt').read().strip().split("\n")
# f = ["qjhvhtzxzqqjkmpb", "xxyxx", "aaa", "aaaa"]

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
    double_indexes = defaultdict(list)
    for i, (a,b) in enumerate(zip(x, x[1:])):
        double_indexes[(a,b)].append(i)
    if all(l[-1] - l[0] < 2 for _, l in double_indexes.items()):
        return False
    return any(a == b for a,b in zip(x, x[2:]))

nice_strings = [x for x in f if process_string(x)]

print(len(nice_strings))

nice_strings = [x for x in f if process_string_2(x)]

print(len(nice_strings))
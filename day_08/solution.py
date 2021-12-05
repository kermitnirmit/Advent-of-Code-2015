f = open("input.txt").read().strip().split("\n")
p1c, p2c = 0, 0
for a in f:
    p1 = a.encode('latin1').decode('unicode-escape')
    quotes = a.count("\"") - 2
    p2 = str(a.encode('latin1')).encode('latin1')
    p1c += len(a) - (len(p1) - 2)
    p2c += len(p2) - len(a) + 1 + quotes
print(p1c)
print(p2c)
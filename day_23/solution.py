from collections import defaultdict

def solve(a_start= 0):
    d = defaultdict(int)
    f = [x for x in open("input.txt").read().strip().split("\n")]
    i = 0
    d["a"] = a_start
    while 0 <= i < len(f):
        # print(i)
        line = f[i].split(" ")
        if len(line) == 3:
            if line[0] == "jie":
                if d[line[1][0]] % 2 == 0:
                    i += int(line[2])
                else:
                    i+=1
            elif line[0] == "jio":
                if d[line[1][0]] == 1:
                    i += int(line[2])
                else:
                    i+= 1
            else:
                i += 1
            # else:
        if len(line) == 2:
            if line[0] == "inc":
                d[line[1]] += 1
            if line[0] == "tpl":
                d[line[1]] *= 3
            if line[0] == "hlf":
                d[line[1]] //= 2
            if line[0] == "jmp":
                i += int(line[1]) - 1
            i+=1
    return d["b"]

print(solve(0))
print(solve(1))
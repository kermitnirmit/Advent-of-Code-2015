p1 = [x.split(" -> ") for x in open("input.txt").read().strip().split("\n")]
p2 = [x.split(" -> ") for x in open("input2.txt").read().strip().split("\n")]


def runPart(f):
    f = [(x[0].split(" "), x[1]) for x in f]
    seen = {}
    i = 0
    s = set(range(339))
    while len(s) > 0:
        if i in s:
            left, right = f[i]

            def handleAndorOr(l, action, r, saveTo):
                if action == "AND":
                    seen[saveTo] = l & r
                else:
                    seen[saveTo] = l | r

            if len(left) == 1 and left[0].isnumeric():
                seen[right] = int(left[0])
                s.remove(i)
            elif len(left) == 1 and left[0] in seen:
                seen[right] = seen[left[0]]
                s.remove(i)
            elif len(left) == 3:
                if left[0] in seen and left[2] in seen:
                    handleAndorOr(seen[left[0]], left[1], seen[left[2]], right)
                    s.remove(i)
                elif left[0] in seen and left[2].isnumeric():
                    if left[1] == "LSHIFT":
                        seen[right] = seen[left[0]] << int(left[2])
                        s.remove(i)
                    if left[1] == "RSHIFT":
                        seen[right] = seen[left[0]] >> int(left[2])
                        s.remove(i)
                elif left[0].isnumeric() and left[2] in seen:
                    handleAndorOr(int(left[0]), left[1], seen[left[2]], right)
                    s.remove(i)
            elif len(left) == 2:
                #     NOT only
                if left[1] in seen:
                    seen[right] = ~ seen[left[1]]
                    if seen[right] < 0:
                        seen[right] += 2 ** 16
                    s.remove(i)
        i += 1
        i = i % len(f)
    return seen["a"]


print("p1 a:", runPart(p1))
print("p2 a:", runPart(p2))

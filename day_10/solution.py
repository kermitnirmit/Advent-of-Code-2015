def solve(end=40):
    f = "1321131112"
    for i in range(end):
        newOne = ""
        count = 1
        prev = 0
        curr = 1
        while curr < len(f):
            if f[curr] != f[prev]:
                newOne += str(count) + f[prev]
            count = count + 1 if f[curr] == f[prev] else 1
            prev += 1
            curr += 1
        newOne += str(count) + f[prev]
        f = newOne
    return len(f)


print(solve(40))
print(solve(50))
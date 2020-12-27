f = open('input.txt').read().strip().split("\n")
#  S = 2(lw + lh + wh)
sides = []
for a in f:
    q,w,e = a.split("x")
    sides.append((int(q),int(w),int(e)))

def smallest_perim(l, w, h):
    qwer = [l, w, h]
    qwer.remove(max(l,w,h))
    return 2 * sum(qwer)

print(sum(2 * (l * w +  l * h + w * h) + + min(l * w, l * h, w * h) for l,w,h in sides))
print(sum(smallest_perim(l, w, h) + (l * w * h) for l,w,h in sides))


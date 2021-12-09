import parse
f = open("input.txt").read().strip().split("\n")

pairing_map = {}

for l in f:
    name, g, num, partner = parse.parse("{} would {} {:d} happiness units by sitting next to {}.", l).fixed
    if name in pairing_map:
        sign = 1 if g == "gain" else -1
        pairing_map[name].append((partner, sign * num))
    else:
        sign = 1 if g == "gain" else -1
        pairing_map[name] = [(partner, sign * num)]

people_left = list(pairing_map.keys())
last = people_left.pop()
print(people_left)
placed = [last]
print(placed)
while len(people_left) != 1:
    m = -10000000
    max_k = -1
    for k, v in pairing_map.items():
        last_score_with_k = [i[1] for i in pairing_map[last] if k in i and k in people_left]
        k_score_with_last = [i[1] for i in pairing_map[k] if last in i and k in people_left]
        if len(last_score_with_k) == 0 or len(last_score_with_k) == 0:
            pass
        else:
            # print(last_score_with_k, k_score_with_last)
            print("found someone", last, k, last_score_with_k, k_score_with_last)
            if k in people_left:
                m = max(m, last_score_with_k[0] + k_score_with_last[0])
                if m == last_score_with_k[0] + k_score_with_last[0]:
                    max_k = k
    last = people_left.pop(people_left.index(max_k))
    placed.append(last)
print("people left", people_left)
placed.extend(people_left)
print(placed)

placed_shifted = placed[1:]
placed_shifted.append(placed[0])

print(placed)
print(placed_shifted)
rsum = 0
for last, k in zip(placed, placed_shifted):
    # rsum
    last_score_with_k = [i[1] for i in pairing_map[last] if k in i][0]
    k_score_with_last = [i[1] for i in pairing_map[k] if last in i][0]

    rsum += last_score_with_k + k_score_with_last
print(rsum)

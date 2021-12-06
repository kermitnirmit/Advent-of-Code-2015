import parse
from collections import defaultdict


class Reindeer:
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest

    def is_resting(self, time):
        return time % (self.duration + self.rest) >= self.duration


things = [Reindeer(n, s, d, r) for n, s, d, r in
          [tuple(parse.parse("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.", x).fixed)
           for x in open("input.txt").read().strip().split("\n")]]

points = defaultdict(int)
distances = {}

def move_thing(t, time):
    # duration + rest = one cycle
    if not t.is_resting(time):
        distances[t] += t.speed


def findMax():
    m = -1
    max_r = []
    for k, v in distances.items():
        m = max(v, m)
    for k, v in distances.items():
        if v == m:
            max_r.append(k)
    return max_r


for i in range(0, 2503):
    for thing in things:
        if thing in distances.keys():
            move_thing(thing, i)
        else:
            distances[thing] = 0
            move_thing(thing, i)
    ma = findMax()
    for r in ma:
        points[r] += 1

m = -1
for k, v in distances.items():
    m = max(v, m)
print(m)

most_points = -1
for k, v in points.items():
    most_points = max(v, most_points)
print(most_points)

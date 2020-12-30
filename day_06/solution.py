from collections import defaultdict
from utils import words
import numpy as np

f = open("input.txt").read().strip().split("\n")
# f = ["toggle 0,0 through 1,1"]
field = np.zeros((1000,1000), dtype=np.int8)

icount = defaultdict(int)
# print(len(f))
for line in f:
    w = line.split()
    # print(w)
    if w[0] == "toggle":
        icount["toggle"] += 1
        sr,sc = w[1].split(",")
        sr = int(sr)
        sc = int(sc)
        er, ec = w[-1].split(",")
        er = int(er)
        ec = int(ec)
        # print(sr, er, sc, ec)
        field[sr:er+1,sc:ec+1] ^= 1
    elif w[1] == "off":
        icount["off"] += 1
        sr,sc = w[2].split(",")
        sr = int(sr)
        sc = int(sc)
        er, ec = w[-1].split(",")
        er = int(er)
        ec = int(ec)
        # print(sr, er, sc, ec)
        field[sr:er+1,sc:ec+1] = 0
    elif w[1] == "on":
        icount["on"] += 1
        sr,sc = w[2].split(",")
        sr = int(sr)
        sc = int(sc)
        er, ec = w[-1].split(",")
        er = int(er)
        ec = int(ec)
        # print(sr, er, sc, ec)
        field[sr:er+1,sc:ec+1] = 1
print(np.sum(field))

brightness = np.zeros((1000,1000), dtype=np.int64)

for line in f:
    w = line.split()
    # print(w)
    if w[0] == "toggle":
        icount["toggle"] += 1
        sr,sc = w[1].split(",")
        sr = int(sr)
        sc = int(sc)
        er, ec = w[-1].split(",")
        er = int(er)
        ec = int(ec)
        # print(sr, er, sc, ec)
        brightness[sr:er+1,sc:ec+1] +=2
    elif w[1] == "off":
        icount["off"] += 1
        sr,sc = w[2].split(",")
        sr = int(sr)
        sc = int(sc)
        er, ec = w[-1].split(",")
        er = int(er)
        ec = int(ec)
        brightness[sr:er+1,sc:ec+1] -= 1 * (brightness[sr:er+1,sc:ec+1] != 0)
    elif w[1] == "on":
        icount["on"] += 1
        sr,sc = w[2].split(",")
        sr = int(sr)
        sc = int(sc)
        er, ec = w[-1].split(",")
        er = int(er)
        ec = int(ec)
        # print(sr, er, sc, ec)
        brightness[sr:er+1,sc:ec+1] += 1

print(np.sum(brightness))
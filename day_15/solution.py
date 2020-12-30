from functools import reduce
from tqdm import tqdm
import operator
f = open("input.txt").read().strip().split("\n")

ingredients = {}

for l in f:
    name, rest = l.split(": ")
    qwer = {}
    for part in rest.split(", "):
        q, v = part.split(" ")
        v = int(v)
        qwer[q] = v
    ingredients[name] = qwer

maxVal = -100000
maxIndexes = [0,0,0,0]

def calculate_score(qwer):
    totalCap = sum(v["capacity"]* qwer[index] for index, (q, v) in enumerate(ingredients.items()))
    totalDur = sum(v["durability"]* qwer[index] for index, (q, v) in enumerate(ingredients.items()))
    totalFlav = sum(v["flavor"]* qwer[index] for index, (q, v) in enumerate(ingredients.items()))
    totalTex = sum(v["texture"]* qwer[index] for index, (q, v) in enumerate(ingredients.items()))
    totalCal = sum(v["calories"]* qwer[index] for index, (q, v) in enumerate(ingredients.items()))
    # comment the next two lines to run part 1
    if totalCal != 500:
        return -100000
    pp = [totalCap, totalDur, totalFlav, totalTex]

    for index in range(4):
        if pp[index] < 0:
            pp[index] = 0
    return reduce(operator.mul, pp, 1)


for i in tqdm(range(101)):
    for j in range(101-i):
        for k in range(101-i-j):
            l = 100-i-j-k
            qwer = [i,j,k,l]
            score = calculate_score(qwer)
            if score > maxVal:
                maxVal = score
                maxIndexes = qwer
print(maxVal)
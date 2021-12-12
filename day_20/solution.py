import numpy as np
from tqdm import trange
l = 34000000


arr = np.zeros(l)
arr_2 = np.zeros(l*2)


for i in trange(1, l):
    for index in range(i, 50*i, i):
        arr_2[index] += 11 * i
    found_asdf = False
    if not found_asdf:
        arr[i::i] += (10 * i)
    if arr_2[i] > l:
        print(i)
        break
    if arr[i] > l and not found_asdf:
        print(i)
        found_asdf = True

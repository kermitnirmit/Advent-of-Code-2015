# row 2978, column 3083
import numpy as np

starting = np.asarray([
    [20151125,  18749137,  17289845,  30943339,  10071777,  33511524],
    [31916031 , 21629792 , 16929656 ,  7726640 , 15514188 ,  4041754],
    [16080970 ,  8057251 ,  1601130 ,  7981243 , 11661866 , 16474243],
    [24592653 , 32451966 , 21345942 ,  9380097 , 10600672 , 31527494],
    [ 77061 , 17552253 , 28094349 ,  6899651 ,  9250759 , 31663883],
    [33071741 ,  6796745 , 25397450 , 24659492 ,  1534922 , 27995004]
])

result = np.zeros((3083*2, 3083*2))

result[:starting.shape[0], :starting.shape[1]] = starting

def getPreviousCoords(i,j):
    n_i, n_j = i + 1, j - 1

    if n_j < 0:
        n_j = n_j + n_i + 1
        n_i = 0
    return (n_i, n_j)

def getNextCoords(i, j):
    n_i, n_j = i - 1, j + 1

    if n_i < 0:
        n_i = n_i + n_j + 1
        n_j = 0
    return (n_i, n_j)

# print(result)

i, j = 6, 0


while i + j <= 2979 + 3083:
    if result[i][j] == 0:
        prev_i, prev_j = getPreviousCoords(i,j)
        result[i][j] = (result[prev_i][prev_j] * 252533) % 33554393
    print(i,j)
    i,j = getNextCoords(i,j)
print(result[2979][3083])
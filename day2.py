from sys import stdin, stdout
# import numpy as np
N = int(input())
# A = np.array([], dtype=int)
A = []
for row in range(N):
    rowval = stdin.readline().strip().split(' ')
    # rowval = np.fromstring(rowval, dtype=int, sep=' ')
    # A = np.append(A, rowval[row])
    A.append(int(rowval[row]))
print(A)


def split_int(listval):
    return list(map(int, listval.split(' ')))


Qlen = int(input())
# prerow = np.array(A)
prerow = A
Qrow = stdin.readlines()
Qrow = list(map(split_int, Qrow))

for line in Qrow:
    a = line[1]
    b = line[2]
    c = line[3]
    array = [c]*(b-a+1)
    for i, array_val in enumerate(array):
        prerow[a-1+i] = prerow[a-1+i] ^ array_val
    # prerow[a-1:b] = prerow[a-1:b] ^ array
    # array = np.ones(b-a+1, dtype=int)*c
    # prerow[a-1:b] = np.bitwise_xor(prerow[a-1:b], array)
# print(prerow.sum())
print(sum(prerow))

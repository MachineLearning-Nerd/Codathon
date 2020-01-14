import pdb
from sys import stdin, stdout
import numpy as np
N = int(input())
A = np.array([], dtype=int)
for row in range(N):
    rowval = stdin.readline()
    rowval = np.fromstring(rowval, dtype=int, sep=' ')
    A = np.append(A, rowval[row])


def Qfunction(N, A):
    Qlen = int(input())
    for row in range(Qlen):
        Qrow = stdin.readline()
        Qrow = np.fromstring(Qrow, dtype=int, sep=' ')
        a = int(Qrow[1])
        b = int(Qrow[2])
        c = int(Qrow[3])
        array1 = np.ones(b-a+1, dtype=int)*c
        yield a, b, array1


prerow = np.array(A)
for a, b, array in Qfunction(N, A):
    prerow[a-1:b] = np.bitwise_xor(prerow[a-1:b], array)


print(prerow.sum())

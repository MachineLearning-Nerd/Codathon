from sys import stdin, stdout
import numpy as np
N = int(input())
A = np.array([], dtype=int)
for row in range(N):
    rowval = stdin.readline()
    rowval = np.fromstring(rowval, dtype=int, sep=' ')
    A = np.append(A, rowval[row])


def split_int(listval):
    return list(map(int, listval.split(' ')))


def Qfunction(N, A):
    Qlen = int(input())
    prerow = np.array(A)
    Qrow = stdin.readlines()
    Qrow = list(map(split_int, Qrow))

    i = 0
    while(i < Qlen):
        line = Qrow[0]
        Qrow.pop(0)
        a = line[1]
        b = line[2]
        c = line[3]
        array = np.ones(b-a+1, dtype=int)*c
        prerow[a-1:b] = np.bitwise_xor(prerow[a-1:b], array)
        i += 1
    print(prerow.sum())


Qfunction(N, A)

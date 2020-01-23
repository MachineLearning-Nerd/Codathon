from sys import stdin, getsizeof
from numpy import bitwise_xor, fromstring, array, append, ones
N = int(input())
A = array([], dtype=int)
for row in range(N):
    rowval = stdin.readline()
    rowval = fromstring(rowval, dtype=int, sep=' ')
    A = append(A, rowval[row])


def Qfunction(N, A):
    Qlen = int(input())
    prerow = array(A)

    for index in range(Qlen):
        line = stdin.readline()
        line = fromstring(line, dtype=int, sep=' ')
        a = line[1]
        b = line[2]
        c = line[3]
        temparray = ones(b-a+1, dtype=int)*c
        prerow[a-1:b] = bitwise_xor(prerow[a-1:b], temparray)
    print(prerow.sum())


Qfunction(N, A)

import pdb
from sys import stdin, stdout
import numpy as np
N = int(input())
A = np.array([], dtype=int)
for row in range(N):
    rowval = stdin.readline()
    rowval = np.fromstring(rowval, dtype=int, sep=' ')
    # rowval = list(map(int, stdin.readline().strip().split(' ')))
    # A.append(rowval[row])
    # import pdb
    # pdb.set_trace()
    A = np.append(A, rowval[row])

Qlen = int(input())
prerow = np.array(A)
for row in range(Qlen):
    # Qrow = stdin.readline().split()
    Qrow = stdin.readline()
    Qrow = np.fromstring(Qrow, dtype=int, sep=' ')
    # print(Qrow)
    a = int(Qrow[1])
    b = int(Qrow[2])
    c = int(Qrow[3])
    array1 = np.ones(b-a+1, dtype=int)*c
    # array2 = np.zeros(a-1, dtype=int)
    # array3 = np.zeros(N-b, dtype=int)
    # newrow = np.append(np.append(array2, array1), array3)
    # import pdb
    # pdb.set_trace()
    # newrow = np.append(np.zeros(a-1, dtype=int),
    #                    np.ones(b-a+1, dtype=int)*c, np.zeros(N-b, dtype=int))
    # import pdb
    # pdb.set_trace()
    prerow[a-1:b] = prerow[a-1:b] ^ array1
print(prerow.sum())

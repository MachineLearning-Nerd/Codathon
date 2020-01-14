from sys import stdin, stdout
N = int(input())
A = []
for row in range(N):
    rowval = stdin.readline().strip().split(' ')
    A.append(int(rowval[row]))


def split_int(listval):
    return list(map(int, listval.split(' ')))


def Qfunction(A):
    Qlen = int(input())
    prerow = A
    # Qrow = stdin.readlines()
    # Qrow = list(map(split_int, Qrow))

    for line in stdin.readlines():
        line = line.strip().split()
        a = int(line[1])
        b = int(line[2])
        c = int(line[3])
        array = [c]*(b-a+1)
        for i, array_val in enumerate(array):
            prerow[a-1+i] = prerow[a-1+i] ^ array_val
    print(sum(prerow))


Qfunction(A)

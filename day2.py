N = int(input())
A = []
for row in range(N):
    rowval = list(map(int, input().split(' ')))
    A.append(rowval)
Qlen = int(input())
for row in range(Qlen):
    Qrow = list(map(int, input().split(' ')))
    a = Qrow[1]
    b = Qrow[2]
    c = Qrow[3]
    for i in range(len(A)):
        if i in range(a-1, b):
            A[i][i] = A[i][i] ^ c
sumval = 0
for i in range(len(A)):
    sumval += A[i][i]
print(sumval)

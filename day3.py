import pdb
from sys import stdin, stdout
import itertools

rowval = list(map(int, stdin.readline().strip().split(' ')))
price = list(map(int, stdin.readline().strip().split(' ')))
n = rowval[0]
m = rowval[1]

data = itertools.product(price, repeat=n)

i = 0
for dataval in data:
    mod = (10**9+7)
    summation = sum(dataval)
    if pow(sum(dataval), 1, m) == 0:
        # print(dataval)
        i += 1
print(i)

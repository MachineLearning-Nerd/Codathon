from sys import stdin, stdout
import itertools

rowval = list(map(int, stdin.readline().strip().split(' ')))
price = list(map(int, stdin.readline().strip().split(' ')))
n = rowval[0]
m = rowval[1]

i = 0
data = itertools.product(price, repeat=n)


def thread_function(data):
    global i
    for x in data:
        if sum(x) % m == 0:
            i += 1


thread_function(data)
print(i)

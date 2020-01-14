from sys import stdin, stdout
import itertools

rowval = list(map(int, stdin.readline().strip().split(' ')))
price = list(map(int, stdin.readline().strip().split(' ')))
n = rowval[0]
m = rowval[1]

data = itertools.product(price, repeat=n)


def summation_map(val):
    if pow(val, 1, m) == 0:
        return 1
    else:
        return 0


def thread_function(data):
    summation = list(map(sum, data))
    output = map(summation_map, summation)
    del summation
    values = list(output)
    return sum(values)


print(thread_function(data))

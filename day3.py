from sys import stdin, stdout
import threading
import itertools

rowval = list(map(int, stdin.readline().strip().split(' ')))
price = list(map(int, stdin.readline().strip().split(' ')))
n = rowval[0]
m = rowval[1]

i = 0
data = itertools.product(price, repeat=n)


def summation_map(val):
    if pow(val, 1, m) == 0:
        return 1
    else:
        return 0


def checking_function(val):
    global i
    if pow(val, 1, m) == 0:
        i += 1


def thread_function(data):
    summation = list(map(sum, data))
    threads = []
    for j in range(len(summation)):
        pop_value = summation.pop(0)
        # print(pop_value)
        x = threading.Thread(target=checking_function, args=(pop_value,))
        threads.append(x)
        x.start()
    for thread in threads:
        thread.join()


thread_function(data)
print(i)

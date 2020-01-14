import pdb
from sys import stdin, stdout
import threading
import itertools

rowval = list(map(int, stdin.readline().strip().split(' ')))
price = list(map(int, stdin.readline().strip().split(' ')))
n = rowval[0]
m = rowval[1]

i = 0
data = itertools.product(price, repeat=n)
print(data)


def thread_function(m):
    global i, data
    for x in data:
        if sum(x) % m == 0:
            i += 1


threads = []
index = 0
while(index < len(price)*len(price)):
    for j in range(10):
        x = threading.Thread(target=thread_function, args=(m,))
        threads.append(x)
        x.start()
    for thread in threads:
        thread.join()
    index += 1


print(i)

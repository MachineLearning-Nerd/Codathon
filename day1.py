def books_on_shelf(data, K):
    while(1):
        if data[0] <= K:
            data.pop(0)
        elif data[-1] <= K:
            data.pop(-1)
        else:
            return len(data)


variables = list(map(int, input().split(' ')))
N = variables[0]
K = variables[1]
data = []
for i in range(N):
    val = int(input().strip())
    data.append(val)
print(books_on_shelf(data, K))

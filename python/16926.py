n, m, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        temp = data[x][y]

        for j in range(i+1, n-i):
            x = j
            change = data[x][y]
            data[x][y] = temp
            temp = change
        for j in range(i+1, m-i):
            y = j
            change = data[x][y]
            data[x][y] = temp
            temp = change
        for j in range(i+1, n-i):
            x = n - j - 1
            change = data[x][y]
            data[x][y] = temp
            temp = change
        for j in range(i+1, m-i):
            y = m - j - 1
            change = data[x][y]
            data[x][y] = temp
            temp = change

for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()

            

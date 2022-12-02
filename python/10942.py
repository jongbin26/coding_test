n = int(input())
arr = list(map(int, input().split()))
palindrom = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(1, (n + 1) - i):
        if i == 0:
            palindrom[j][j+i] = 1
        elif i == 1:
            if arr[j - 1] == arr[j + i - 1]:
                palindrom[j][j+i] = 1
        else:
            if palindrom[j+1][j+i-1] == 1 and arr[j-1] == arr[j+ i -1]:
                palindrom[j][j+i] = 1

ans = []
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    ans.append(palindrom[a][b])
for i in ans:
    print(i)
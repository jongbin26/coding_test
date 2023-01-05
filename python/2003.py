n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt, temp, j = 0, 0, 0
for i in range(n):
    while temp < m and j < n:
        temp += arr[j]
        j += 1
    if temp == m:
        cnt += 1
    temp -= arr[i]
print(cnt)
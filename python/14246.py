n = int(input())
arr = list(map(int, input().split()))
k = int(input())

cnt, temp, j = 0, 0, 0
for i in range(n):
    while(temp <= k and j < n):
        temp += arr[j]
        j += 1
    if temp > k:
        temp -= arr[i]
        cnt += n - j + 1
        continue
    else:
        break
print(cnt)
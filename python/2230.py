import sys
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
j, temp, ans = 0, -1, sys.maxsize
for i in range(n):
    while(j < n):
        temp = arr[j] - arr[i]
        if temp >= m:
            break
        else:
            j += 1
    if temp >= m:
        ans = min(ans, temp)
        temp = -1
print(ans)
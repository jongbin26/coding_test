n, k = map(int, input().split())
length = 1000001
arr = [0] * length
for _ in range(n):
    g, x = map(int, input().split())
    arr[x] = g
temp = sum(arr[0:2*k+1])
ans = sum(arr[0:2*k+1])
for i in range(k, length - k - 1):
    temp = temp - arr[i-k] + arr[i+k+1]
    ans = max(ans, temp)
print(ans)
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans, temp_sum = sum(arr[0:k]), sum(arr[0:k])
for i in range(1, n-k+1):
    temp_sum = temp_sum - arr[i-1] + arr[i+k-1]
    ans = max(ans, temp_sum)
print(ans)
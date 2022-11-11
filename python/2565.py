n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : x[0])

dp = [0] * len(arr)
dp[0] = 1
for i in range(1, len(dp)):
    max_num = 0
    for j in range(0, i):
        if arr[j][1] < arr[i][1]:
            max_num = max(max_num, dp[j])
    dp[i] = max_num + 1

print(len(dp)-max(dp))
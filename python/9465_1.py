t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    table = []
    for _ in range(2):
        table.append(list(map(int, input().split())))
    if n == 1:
        ans.append(max(table[0][0], table[1][0]))
        continue
    if n == 2:
        ans.append(max(table[1][0] + table[0][1], table[0][0] + table[1][1]))
        continue
    dp = [[0] * n for _ in range(2)]
    dp[0][0], dp[1][0] = table[0][0], table[1][0]
    dp[0][1], dp[1][1] = table[1][0] + table[0][1], table[0][0] + table[1][1]
    for i in range(2, n):
        dp[0][i] = table[0][i] + max(max(dp[0][i-2], dp[1][i-2]), dp[1][i-1])
        dp[1][i] = table[1][i] + max(max(dp[0][i-2], dp[1][i-2]), dp[0][i-1])
    ans.append(max(dp[0][-1], dp[1][-1]))
[print(i) for i in ans]
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]
dp[0][0] = graph[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = graph[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = graph[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = graph[i][j] + max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[n-1]))
T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    
    if n == 1:
        ans.append(max(graph[0][0], graph[1][0]))
    elif n == 2:
        ans.append(max(graph[1][0] + graph[0][1], graph[0][0] + graph[1][1]))
    else:
        dp[0][0], dp[1][0] = graph[0][0], graph[1][0]
        dp[0][1], dp[1][1] = graph[1][0] + graph[0][1], graph[0][0] + graph[1][1]
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-2] + graph[0][i], dp[1][i-1] + graph[0][i])
            dp[1][i] = max(dp[0][i-2] + graph[1][i], dp[0][i-1] + graph[1][i])
        ans.append(max(max(dp[0]), max(dp[1])))
        
for i in ans:
    print(i)
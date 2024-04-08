import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int , sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]
def dfs(x):
    visited[x] = 1
    if not graph[x]:
        dp[x][1] = 1
        dp[x][0] = 0
    else:
        for i in graph[x]:
            if visited[i] == 0:
                dfs(i)
                dp[x][1] += min(dp[i][0], dp[i][1])
                dp[x][0] += dp[i][1]
        dp[x][1] += 1
dfs(1)
print(min(dp[1][0], dp[1][1]))
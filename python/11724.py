n, m = map(int ,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n+1)
def dfs(x):
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)
ans = 0
for i in range(1, n+1):
    if not visited[i]:
        ans += 1
        dfs(i)
print(ans)
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n

ans = int(1e9)

def dfs(x, idx):
    global ans
    if x == n // 2:
        team1, team2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    team1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += graph[i][j]
        ans = min(ans, abs(team1 - team2))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(x+1, i+1)
            visited[i] = False
            
dfs(0, 0)
print(ans)
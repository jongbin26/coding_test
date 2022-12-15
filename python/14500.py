n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt, total, visited):
    global ans
    visited[x][y] = 1
    total += graph[x][y]
        
    if cnt >= 3:
        ans = max(ans, total)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                dfs(nx, ny, cnt + 1, total, visited)

ans = 0
for i in range(n):
    for j in range(m):
        visited = [[0] * m for _ in range(n)]
        dfs(i, j, 0, 0, visited)
print(ans)
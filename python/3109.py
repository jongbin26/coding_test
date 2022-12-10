n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]

dx = [-1, 0, 1]
dy = [1, 1, 1]
visited = [[0] * m for _ in range(n)]
ans = 0
def dfs(x, y):
    global ans, stop
    if y == m - 1:
        ans += 1
        stop = True
        return
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if not stop:
            if 0 <= nx < n and 0 < ny < m:
                if graph[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dfs(nx, ny)
for i in range(n):
    stop = False
    dfs(i, 0)
print(ans)
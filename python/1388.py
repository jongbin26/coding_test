n, m = map(int ,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, type):
    if type == '|':
        for i in range(0, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == type:
                    visited[nx][ny] = 1
                    dfs(nx, ny, type)
    else:
        for i in range(2, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == type:
                    visited[nx][ny] = 1
                    dfs(nx, ny, type)
    return
ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            ans += 1
            dfs(i, j, graph[i][j])
print(ans)
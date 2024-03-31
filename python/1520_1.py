m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

visited = [[-1] * (n) for _ in range(m)]

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    temp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m and 0 <= ny < n):
            if graph[nx][ny] < graph[x][y] :
                temp += dfs(nx, ny)
        visited[x][y] = temp
    return visited[x][y]

print(dfs(0, 0))
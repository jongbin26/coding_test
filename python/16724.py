n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

visited = [[0] * (m) for _ in range(n)]
def dfs(x, y):
    global ans
    visited[x][y] = 1
    cycle.append([x, y])

    if graph[x][y] == 'L' and y > 0:
        nx, ny = x, y-1
    elif graph[x][y] == 'R' and y < m-1:
        nx, ny = x, y+1
    elif graph[x][y] == 'D' and x < n-1:
        nx, ny = x+1, y
    elif graph[x][y] == 'U' and x > 0:
        nx, ny = x-1, y

    if visited[nx][ny]:
        if [nx, ny] in cycle:
            ans += 1
    else:
        dfs(nx, ny)
ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cycle = []
            dfs(i, j)
print(ans)
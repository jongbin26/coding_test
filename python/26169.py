graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))
r, c = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * 5 for _ in range(5)]

ans = False
def dfs(x, y, move , count):
    global ans
    if move > 3:
        return
    if count == 2:
        ans = True
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if not visited[nx][ny] and graph[nx][ny] != -1:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    graph[x][y] = -1
                    dfs(nx, ny, move+1, count+1)
                    graph[x][y] = 1
                    visited[nx][ny] = 0
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    graph[x][y] = -1
                    dfs(nx, ny, move+1, count)
                    graph[x][y] = 0
                    visited[nx][ny] = 0
dfs(r, c, 0, 0)
if ans:print(1)
else:print(0)
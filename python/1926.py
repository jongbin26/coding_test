from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*(m) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
max_draw = 0
def bfs(x, y):
    global max_draw
    queue = deque()
    temp = 1
    visited[x][y] = 1
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    temp += 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    max_draw = max(temp, max_draw)
    return max_draw
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            bfs(i, j)
print(cnt)
print(max_draw)
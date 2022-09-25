from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(str, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append((nx, ny))
    return max(map(max, visited))

ans = 0
for i in range(n):
    for j in range(m):
        visited = [[0] * m for _ in range(n)]
        if graph[i][j] == 'L':
            ans = max(ans, bfs(i, j))
print(ans-1)
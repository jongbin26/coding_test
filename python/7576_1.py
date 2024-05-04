from collections import deque
n, m = map(int ,input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(visited):
    max = -1
    for i in range(m):
        for j in range(n):
            if visited[i][j] >= max:
                max = visited[i][j]
            if visited[i][j] == 0 and graph[i][j] != -1:
                return -1
    return max
    

def bfs(tomatoes):
    queue = deque()
    for x in tomatoes:
        queue.append((x[0], x[1]))
        visited[x[0]][x[1]] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if( 0 <= ny < n and 0 <= nx < m):
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

tomatoes = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            tomatoes.append([i, j])
visited = [[0] * n for _ in range(m)]
bfs(tomatoes)
temp = check(visited)
if temp > 0:
    print(temp-1)
else: print(temp)

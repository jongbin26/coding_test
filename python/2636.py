from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                return True
    return False

def count():
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count += 1
    return count

def bfs(x, y):
    global melt
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                if graph[nx][ny] == 1:
                    melt.append((nx, ny))

time = 0
space = 0
while True:
    visited = [[0] * m for _ in range(n)]
    melt = []
    bfs(0, 0)
    time += 1
    before_count = count()
    for x, y in melt:
        graph[x][y] = 0
    after_count = count()
    if not after_count:
        space = before_count
        break
    
print(time)
print(space)
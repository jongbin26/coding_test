from collections import deque
n, m = map(int ,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

ans = 0
def bfs(x, y):
    countable = True
    global ans
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if graph[x][y] > 1:
            countable = False
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] > 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return countable

def finish():
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                return False
    return True

def minus():
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                graph[i][j] -= 1

def print_graph():
    for i in range(n):
        for j in range(m):
            print(graph[i][j], end=' ')
        print()
while(not finish()):
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] > 0:
                visited[i][j] = True
                if(bfs(i, j)):
                    ans +=1
    minus()
print(ans)
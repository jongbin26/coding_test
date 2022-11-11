import copy
from collections import deque
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global unite
    total, count = 0, 0
    queue = deque()
    queue.append((x, y))
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    total += graph[nx][ny]
                    count += 1
                    visited[nx][ny] = unite
                    queue.append((nx, ny))
    if count > 0:
        devide = total // count
        for i in range(n):
            for j in range(n):
                if visited[i][j] == unite:
                    copy_graph[i][j] = devide
    unite += 1
    
def finish_check():
    finish_bool = True
    for i in range(n):
        for j in range(n):
            if visited[i][j] > 0:
                finish_bool = False
                return finish_bool
    return finish_bool

t = 0

while(True):
    unite = 1
    visited = [[0] * n for _ in range(n)]
    copy_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            bfs(i, j)
    graph = copy.deepcopy(copy_graph)
    if finish_check():
        print(t)
        exit()
    t += 1
    
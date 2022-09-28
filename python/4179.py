import sys
from collections import deque
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sg, fire_points):
    queue = deque()
    graph[sg[0]][sg[1]] = 0
    for point in fire_points:
        queue.append((point[0], point[1], True))
    queue.append((sg[0], sg[1], False))
    while(queue):
        x, y, is_fire = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if is_fire:
                    if graph[nx][ny] != '#' and graph[nx][ny] != 'F':
                        graph[nx][ny] = 'F'
                        queue.append((nx, ny, True))
                else:
                    if graph[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny, False))
            else:
                if not is_fire:
                    return visited[x][y]+1

graph = []
r, c = map(int, sys.stdin.readline().split())
for _ in range(r):
    graph.append(list(map(str, sys.stdin.readline())))
fire_points = []
visited = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            sg = [i, j]
        elif graph[i][j] == 'F':
            fire_points.append([i, j])
res = bfs(sg, fire_points)

if res:
    print(res)
else:
    print('IMPOSSIBLE')
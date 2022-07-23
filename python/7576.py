from collections import deque
m, n = map(int, input().split())
graph = []
[graph.append(list(map(int, input().split()))) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((j, i))
    
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))

bfs()
ans = True
for i in graph:
    for j in i:
        if j == 0:
            ans = False
            
if ans == False:
    print(-1)
else:
    print(max(map(max, graph))-1)
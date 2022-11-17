from collections import deque
n , k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

visited = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    virus = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                virus.append([i, j, graph[i][j]])
    virus.sort(key = lambda x : x[2])
    for i in virus:
        visited[i[0]][i[1]][0] = i[2]
        queue.append((i[0], i[1], i[2]))
    while(queue):
        x, y, value = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny][0] == 0:
                    visited[nx][ny][0] = value
                    visited[nx][ny][1] = visited[x][y][1] + 1
                    queue.append((nx, ny, value))
                    
bfs()
if s < visited[x-1][y-1][1]:
    print(0)
else:
    print(visited[x-1][y-1][0])
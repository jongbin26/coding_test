from collections import deque
n = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def fire(x, y):
    queue = deque()
    queue.append((x, y))
    fire_visited[x][y] = 1
    while(queue):
        x, y = queue.popleft()
        nx = x + dx[i]
        ny = y + dy [i]
        if 0 <= nx < h and 0 <= ny < w:
            if fire_visited[nx][ny] == 0:
                fire_visited[nx][ny] = 1
                graph[nx][ny] = '*'
                queue.append((nx, ny))
        
def 
for _ in range(n):
    graph = []
    w, h = map(int, input().split())
    for _ in range(h):
        graph.append(list(map(str, input())))
    
    fire_visited = [[0] * w for _ in range(h)]
	visited = [[0] * w for _ in range(h)]
    


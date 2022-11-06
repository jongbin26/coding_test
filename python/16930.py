from collections import deque
n, m, k = map(int, input().split())
inf = 1000000
visited = [[inf] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = [list(map(str, input())) for _ in range(n)]
x1,y1,x2,y2 = map(int,input().split())
def bfs(x, y):
    queue = deque()
    queue.append((x1-1, y1-1))
    visited[x1-1][y1-1] = 0
    
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cnt = 1
            while cnt <= k and 0 <= nx < n and 0 <= ny < m and graph[nx][ny] =='.' and visited[nx][ny] > visited[x][y]:
                if visited[nx][ny] == inf:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                nx += dx[i]
                ny += dy[i]
                cnt += 1
                
bfs(x1, y1)
if visited[x2-1][y2-1] == inf:
    print(-1)
else:
    print(visited[x2-1][y2-1])
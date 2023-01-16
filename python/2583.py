from collections import deque
m, n, k = map(int, input().split())
areas = [list(map(int, input().split())) for _ in range(k)]

graph = [[0] * n for _ in range(m)]
for area in areas:
    x1, y1, x2, y2 = area[0], area[1], area[2], area[3]
    for i in range(x1, x2):
        for j in range(y1, y2):
            if graph[j][i] == 0:
                graph[j][i] = 1
                
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * n for _ in range(m)]
def bfs(x, y):
    cnt = 1
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    cnt += 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return cnt
ans = []
ans_cnt = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 0:
            ans_cnt += 1
            ans.append(bfs(i, j))
ans.sort()
print(ans_cnt)
for i in ans:
    print(i, end=' ')
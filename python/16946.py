from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0] * m for _ in range(n)]
def bfs(x, y, cnt):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = cnt
    area = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = cnt
                    queue.append((nx, ny))
                    area += 1
    return area
category = {}
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 0:
            cnt += 1
            category[cnt] = bfs(i, j, cnt)
ans = [[0] * m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            temp = 0
            check = []
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] > 0:
                        if visited[nx][ny] not in check:
                            temp += category[visited[nx][ny]]
                            check.append(visited[nx][ny])
            ans[x][y] = temp + 1
                

for i in range(n):
    for j in range(m):
        print(ans[i][j]%10, end='')
    print()
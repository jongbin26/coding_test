import copy
from collections import deque
n, l, r = map(int, input().split())
graph = []
for _ in range(2):
    graph.append(list(map(int, input().split())))
origin = copy.deepcopy(graph)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, k):
    sum, cnt = 0, 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = k
                    cnt += 1
                    sum += graph[nx][ny]
                    queue.append((nx, ny))
    return [sum, cnt]
k = 0
ans = 0
while True:
    graph = origin
    visited = [[0] * n for _ in range(n)]
    x = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                k += 1
                temp = bfs(i, j, k)
                if temp[0] > 0:
                    x.append(temp)
                for l in range(n):
                    for m in range(n):
                        if visited[l][m] == k and temp[0] > 0:
                            graph[l][m] = temp[0] // temp[1]
    if not x:
        break
    else: ans += 1

print(graph)
print(ans)
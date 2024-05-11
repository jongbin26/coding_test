from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, count):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = count
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = count
                    queue.append((nx, ny))
count = 0
visited = [[0] * (n) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            count += 1
            bfs(i, j, count)
ans = [0] * (count + 1)
for c in range(1, count+1):
    for i in visited:
        ans[c] += i.count(c)
print(count)
ans.sort()
ans = ans[1:]
for i in ans:
    print(i)
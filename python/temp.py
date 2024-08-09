from collections import deque

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

with_gram = 0
without_gram = 0

def bfs(x, y):
  global with_gram, without_gram
  q = deque([(x, y)])
  visited[x][y] = 1
  while q:
    x, y = q.popleft()
    if x == n - 1 and y == m - 1:
      if visited[x][y] <= t:
        without_gram = visited[x][y] - 1
        return
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 2 and visited[nx][ny] == 0:
          with_gram = visited[x][y] + (n-1) - nx + (m-1) - ny
          if t < with_gram:
            with_gram = 0
          visited[nx][ny] = -1
        elif graph[nx][ny] == 0 and visited[nx][ny] == 0:
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx, ny))
  
bfs(0,0)

if not with_gram and not without_gram:
  print("Fail")
elif with_gram and not without_gram:
  print(with_gram)
elif not with_gram and without_gram:
  print(without_gram)
elif with_gram and without_gram:
  print(min(with_gram,without_gram))
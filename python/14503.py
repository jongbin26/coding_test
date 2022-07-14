import sys
from collections import deque
sys.setrecursionlimit(15000)

def turn(d):
    d -= 1
    if d < 0:
        d += 4
    return d
    
def dfs(x, y, d):
    visited[x][y] = 1
    
    for _ in range(4):
        d = turn(d)
        nx = x + dx[d]
        ny = y + dy[d]
        
        if visited[nx][ny] == 0 and graph[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, d)
    
        

n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = []
visited = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]	

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)]for _ in range(n)]

dfs(r, c, d)
total = 0
for row in visited:
    for j in row:
        if j == 1:
            total += 1
print(total)
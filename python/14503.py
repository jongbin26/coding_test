import sys
from collections import deque
sys.setrecursionlimit(15000)

def turn(d):
    d -= 1
    if d < 0:
        d += 4
    return d        

def dfs(x, y, d):
    global total
    if visited[x][y] == 0 and graph[x][y] == 0:
        visited[x][y] = 1
        total += 1
    
    for _ in range(4):
        nd = turn(d)
        nx = x + dx[nd]
        ny = y + dy[nd]
        if visited[nx][ny] == 0 and graph[nx][ny] == 0:
            dfs(nx, ny, nd)
            return
        d = nd
    nd = turn(turn(d))
    nx = x + dx[nd]
    ny = y + dy[nd]
    if graph[nx][ny] == 1:
        return
    dfs(nx, ny, d)
    



n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
visited = []
total = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]	

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)]for _ in range(n)]

dfs(x, y, d)
print(total)
import sys
sys.setrecursionlimit(1000000)
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(color, x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if visited[nx][ny] == 0 and graph[nx][ny] == color:
                dfs(color, nx, ny)

def size():
    ans = 0
    for i in range(N):
    	for j in range(N):
            if visited[i][j] == 0:
                dfs(graph[i][j], i, j)
                ans += 1
    return ans

def blind():
    global N
    for i in range(N):
    	for j in range(N):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'

result = []
visited = [[0]*N for _ in range(N)]
result.append(size())
blind()
visited = [[0]*N for _ in range(N)]
result.append(size())
print(result[0], result[1])
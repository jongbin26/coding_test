import sys
from collections import deque
import copy
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def make(x, y):
    visited[x][y] = 1
    graph[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and ((graph[nx][ny] == 0) or (graph[nx][ny] == 2)):
                make(nx, ny)
                
def air(x, y):
    delete = 0
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 2:
                count += 1
    if count >= 2:
        delete = 1
    return delete
time = 0
while(True):
    ans_bool = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                ans_bool = 0
    if ans_bool:
        break
    time += 1
    visited = [[0] * m for _ in range(n)]
    make(0, 0)
    change_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                if air(i, j):
                    change_graph[i][j] = 2
    graph = copy.deepcopy(change_graph)
print(time)
import itertools
from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int ,input().split())))

temp = []
viruses = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            temp.append((i, j))
        if graph[i][j] == 2:
            viruses.append((i, j))
barriers_comb = list(itertools.combinations(temp, 3))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    queue = deque()
    for virus in viruses:
        queue.append(virus)
        visited[virus[0]][virus[1]] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

def print_graph():
    for i in range(n):
        for j in range(m):
            print(visited[i][j], end=' ')
        print()
max_ans = 0
for barriers in barriers_comb:
    for barrier in barriers:
        graph[barrier[0]][barrier[1]] = 1
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    bfs()
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and graph[i][j] != 1:
                cnt += 1
    for barrier in barriers:
        graph[barrier[0]][barrier[1]] = 0
    if cnt >= max_ans:
        max_ans = cnt
print(max_ans)
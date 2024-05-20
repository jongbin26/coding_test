from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny]:
                    if graph[nx][ny] == '.':
                        queue.append([nx, ny])
                    else:   #빙판인 경우에 다음 번에 물이 되므로 임시 큐에 삽입
                        queue_temp.append([nx, ny])
                    visited[nx][ny] = 1
    return 0

def melt():
    while w_queue:
        x, y = w_queue.popleft()
        if graph[x][y] == 'X':
            graph[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not w_visited[nx][ny]:
                    if graph[nx][ny] == 'X':
                        w_queue_temp.append([nx, ny])   #빙판이면 다음번에 물로 바꿔줘야 하므로 임시 w_queue에 삽입
                    else:
                        w_queue.append([nx, ny])
                    w_visited[nx][ny] = 1
m, n = map(int, input().split())
visited = [[0]*n for _ in range(m)]
w_visited = [[0]*n for _ in range(m)]

graph, swan = [], []
queue, queue_temp, w_queue, w_queue_temp = deque(), deque(), deque(), deque()

for i in range(m):
    row = list(input().strip())
    graph.append(row)
    for j, k in enumerate(row):
        if graph[i][j] == 'L':
            swan.extend([i, j])
            w_queue.append([i, j])
        elif graph[i][j] == '.':
            w_visited[i][j] = 1
            w_queue.append([i, j])

x1, y1, x2, y2 = swan
queue.append([x1, y1])
graph[x1][y1], graph[x2][y2], visited[x1][y1] = '.', '.', 1
cnt = 0

while True:
    melt()
    if bfs():
        print(cnt)
        break
    queue, w_queue = queue_temp, w_queue_temp   #다음 턴 : queue_temp에 있던 백조 이동 가능 경로, w_queue_temp에 있던 이제 녹을 빙판 대치
    queue_temp, w_queue_temp = deque(), deque()
    cnt += 1
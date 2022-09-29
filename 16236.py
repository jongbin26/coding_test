from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def paint(visited):
    for i in range(n):
        for j in range(n):
            print(visited[i][j], end='')
        print()
    print("-----------------")

ans, count, size = 0, 0, 2
def bfs(x, y):
    flag = True
    short = []
    graph[x][y] = 0
    global ans, size, count
    visited = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if 0 < graph[nx][ny] < size and visited[nx][ny] == 0:
                    flag = False
                    graph[nx][ny] = 0
                    visited[nx][ny] = visited[x][y] + 1
                    paint(visited)
                    ans += visited[nx][ny]
                    count += 1
                    if count >= size:
                        size += 1
                        count = 0
                    short.append([nx, ny])
                elif (graph[nx][ny] == size or graph[nx][ny] == 0) and visited[nx][ny] == 0 and flag:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    if short:
        short.sort(key = lambda a : a[0], reverse=True)
        return short[0]
    else:
        return 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            #시작 조건
            res = bfs(i, j)
            while(res):
                res = bfs(res[0], res[1])
                
print(ans)
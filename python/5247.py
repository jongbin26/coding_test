from collections import deque
n = int(input())
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sg, fire_points):
    queue = deque()
    graph[sg[0]][sg[1]] = 0
    for point in fire_points:
        queue.append((point[0], point[1], True))
    queue.append((sg[0], sg[1], False))
    while(queue):
        x, y, is_fire = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if is_fire:
                    #큐에서 뺀 게 불인 경우
                    if graph[nx][ny] != '#' and graph[nx][ny] != '*':
                        graph[nx][ny] = '*'
                        queue.append((nx, ny, True))
                else:
                    #큐에서 뺀 게 상근이인 경우
                    if graph[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny, False))
            else:
                if not is_fire:
                    #상근이 탈출
                    return visited[x][y]+1

ans = []
for _ in range(n):
    graph = []
    w, h = map(int, input().split())
    for _ in range(h):
        graph.append(list(map(str, input())))
    fire_points = []
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                sg = [i, j]
            elif graph[i][j] == '*':
                fire_points.append([i, j])
    res = bfs(sg, fire_points)
    if res:
        ans.append(res)
    else:
        ans.append('IMPOSSIBLE')
    
for i in ans:
    print(i)
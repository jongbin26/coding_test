from collections import deque
n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = []

def roll(x, y, i):
    dist = 0
    while(True):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[nx][ny] == "#":
            return x, y, dist
        elif graph[nx][ny] == "O":
            return nx, ny, dist
        else:
            x, y = nx, ny
            dist += 1

def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by, 1))
    visited.append([rx, ry, bx, by])
    while(queue):
        rx, ry, bx, by, cnt = queue.popleft()
        if cnt > 10:
            print(-1)
            exit(0)
        
        for i in range(4):
            nrx, nry, rdist = roll(rx, ry, i)
            nbx, nby, bdist = roll(bx, by, i)
            
            if graph[nbx][nby] == "O":
                continue
            else:
                if graph[nrx][nry] == "O":
                    print(cnt)
                    exit(0)
            
            if nrx == nbx and nry == nby:
                if rdist > bdist:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if [nrx, nry, nbx, nby] not in visited:
                queue.append((nrx, nry, nbx, nby, cnt + 1))
                visited.append([nrx, nry, nbx, nby])
    print(-1)

for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            rx, ry = i, j
        if graph[i][j] == "B":
            bx, by = i, j
        if graph[i][j] == "O":
            hx, hy = i, j
bfs(rx, ry, bx, by)
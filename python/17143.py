R, C, M = map(int, input().split())
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
graph = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[r-1][c-1].append([s, d-1, z])

def move():
    g = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                x, y = i, j
                s, d, z = graph[i][j][0]
                dist = s
                while 0 < dist:
                    nx = x + direction[d][0]
                    ny = y + direction[d][1]
                    if 0 <= nx < R and 0 <= ny < C:
                        x, y = nx, ny
                        dist -= 1
                    else:
                        if d == 0 or d == 2:
                            d += 1
                        elif d == 1 or d == 3:
                            d -= 1
                        continue
                g[x][y].append([s, d, z])

    for i in range(R):
        for j in range(C):
            graph[i][j] = g[i][j]

def catch():
    global ans
    for i in range(C):
        for j in range(R):
            if graph[j][i]:
                ans += graph[j][i][0][2]
                graph[j][i].remove(graph[j][i][0])
                break #필요한가?
        move()
        for m in range(R):
            for n in range(C):
                if len(graph[m][n]) > 1:
                    graph[m][n].sort(key = lambda x:x[2], reverse=True)
                    while len(graph[m][n]) > 1:
                        graph[m][n].pop()

 

ans = 0
catch()
print(ans)

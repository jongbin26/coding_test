import copy
r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

cleaner = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:
            cleaner.append([i, j])

def diffuse(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if not ((nx == cleaner[0][0] and ny == 0) or (nx == cleaner[1][0] and ny == 0)):
                temp[nx][ny] += graph[x][y] // 5
                count += 1
    temp[x][y] -= (graph[x][y] // 5) * count

def clean():
    #윗 공기청정기
    for i in range(cleaner[0][0]-1, 0, -1):
        graph[i][0] = graph[i-1][0]
    for i in range(c-1):
        graph[0][i] = graph[0][i+1]
    for i in range(0, cleaner[0][0]):
        graph[i][c-1] = graph[i+1][c-1]
    for i in range(c-1, 0, -1):
        graph[cleaner[0][0]][i] = graph[cleaner[0][0]][i-1]
    graph[cleaner[0][0]][1] = 0
    #아래 공기청정기
    for i in range(cleaner[1][0]+1, r-1):
        graph[i][0] = graph[i+1][0]
    for i in range(c-1):
        graph[r-1][i] = graph[r-1][i+1]
    for i in range(r-1, cleaner[1][0], -1):
        graph[i][c-1] = graph[i-1][c-1]
    for i in range(c-1, 0, -1):
        graph[cleaner[1][0]][i] = graph[cleaner[1][0]][i-1]
    graph[cleaner[1][0]][1] = 0

for i in range(t):
    temp = copy.deepcopy(graph)
    for i in range(r):
        for j in range(c):
            if graph[i][j] != -1 and graph[i][j] != 0:
                diffuse(i, j)
    graph = copy.deepcopy(temp)
    clean()
    
def total():
    ans = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] != -1 and graph[i][j] != 0:
                ans+=graph[i][j]
    return ans

print(total())
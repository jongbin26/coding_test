import copy
r, c, n = map(int, input().split())
temp = [list(map(str, input())) for _ in range(r)]
graph = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if temp[i][j] == '.':
            graph[i][j] = -1
        else:
            graph[i][j] = 3
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def paint():
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                print('O', end='')
            else:
                print('.', end='')
        print()
def explosion():
    global graph
    temp = copy.deepcopy(graph)
    for i in range(r):
            for j in range(c):
                if graph[i][j] == 0:
                    temp[i][j] = -1
                    for k in range(4):
                        ni = i + dx[k]
                        nj = j + dy[k]
                        if 0 <= ni < r and 0 <= nj < c:
                            temp[ni][nj] = -1
    graph = copy.deepcopy(temp)
for t in range(1, n+1):
    if t == 1:
        for i in range(r):
            for j in range(c):
                if graph[i][j] > 0:
                    graph[i][j] -= 1
        continue
    if t % 2 == 0:
        #설치
        for i in range(r):
            for j in range(c):
                if graph[i][j] == -1:
                    graph[i][j] = 3
                else:
                    graph[i][j] -= 1
        explosion()
    else:
        #폭발
        for i in range(r):
            for j in range(c):
                if graph[i][j] > 0:
                    graph[i][j] -= 1
        explosion()
paint()
from itertools import combinations
import copy
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
zero_list = []

#0 좌표 구하기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_list.append([i, j])
#조합
case = list(combinations(zero_list, 3))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and nx < n and ny >= 0 and ny < m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx, ny)

ans = 0
for wall_list in case:
    result = 0
    tmp = copy.deepcopy(graph)
    for wall in wall_list:
        tmp[wall[0]][wall[1]] = 1
    
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                virus(i, j)
    
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                result += 1
    
    ans = max(result, ans)
print(ans)
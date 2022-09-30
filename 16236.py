from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

size, count, ans = 2, 0, 0
def bfs(x, y):
    short = []
    flag = True
    min_dist = 100000000000
    global size, count, ans
    visited = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                #최단거리 먹을 수 있는 물고기 칸 -> 같은 거리에 있으면 왼쪽
                if 0 < graph[nx][ny] < size and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    if min_dist >= visited[nx][ny]:
                        min_dist = visited[nx][ny]
                        short.append([nx, ny])
                    flag = False
                #비어있는 칸(0)이거나 size 같은 물고기 칸 + 다른 칸에서 물고기를 먹었다면 flag=False가 되어 더이상 queue에 추가 x
                elif (graph[nx][ny] == 0 or graph[nx][ny] == size) and visited[nx][ny] == 0 and flag:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    if short:
        short.sort()
        count += 1
        if count >= size:
            size += 1
            count = 0
        ans += visited[short[0][0]][short[0][1]]
        graph[short[0][0]][short[0][1]] = 0
        return [short[0][0], short[0][1]]
    else:
        return 0
    
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            res = bfs(i, j)
            while(res):
                res = bfs(res[0], res[1])
print(ans)
                
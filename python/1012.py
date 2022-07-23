t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    visited[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n:
            if visited[ny][nx] == 0 and [nx, ny] in a:
                bfs(nx, ny)
    return True

ans = []
for _ in range(t):
    m, n, k = map(int, input().split())
    a = []
    [a.append(list(map(int, input().split()))) for _ in range(k)]
    visited = [[0] * m for _ in range(n)]
    
    res = 0
    for i in a:
        if visited[i[1]][i[0]] == 0:
            bfs(i[0], i[1])
            res+=1
    ans.append(res)

for i in ans:
    print(i)
    
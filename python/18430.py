n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
if n < 2 or m < 2:
    print(0)
    exit()
visited = [[0] * m for _ in range(n)]
ans = 0
dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]
def dfs(x, y, total):
    global ans
    if y == m:
        x, y = x+1, 0
    if x == n:
        ans = max(ans, total)
        return
    if not visited[x][y]:
        for i in range(4):
            if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m:
                if visited[x+dx[i]][y] == 0 and visited[x][y+dy[i]] == 0:
                    visited[x][y], visited[x+dx[i]][y], visited[x][y+dy[i]] = 1, 1, 1
                    dfs(x, y+1, total+2*graph[x][y]+graph[x+dx[i]][y]+graph[x][y+dy[i]])
                    visited[x][y], visited[x+dx[i]][y], visited[x][y+dy[i]] = 0, 0, 0
    dfs(x, y+1, total)
dfs(0, 0, 0)
print(ans)
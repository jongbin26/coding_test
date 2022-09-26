from collections import deque
r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(str, input())))
alpha = [0] * 26
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global max_len, count
    max_len = max(max_len, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if alpha[ord(graph[nx][ny])-ord('A')] == 0:
                count += 1
                alpha[ord(graph[nx][ny])-ord('A')] = 1
                dfs(nx, ny)
                count -= 1
                alpha[ord(graph[nx][ny])-ord('A')] = 0
                
max_len = 0
count = 1
alpha[ord(graph[0][0])-ord('A')] = 1
dfs(0, 0)
print(max_len)

                    
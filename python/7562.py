from collections import deque
t = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y, n):
    visited = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y, 0))
    while(queue):
        x, y, cnt = queue.popleft()
        if x == end[0] and y == end[1]:
            return cnt
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, cnt+1))
ans = []
for _ in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    ans.append(bfs(start[0], start[1], n))

for i in ans:
    print(i)
                    
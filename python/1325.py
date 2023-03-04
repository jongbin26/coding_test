from collections import deque
n, m = map(int, input().split())
relation = [list(map(int, input().split())) for _ in range(m)]
edge = [[] for _ in range(n+1)]
for i in relation:
    edge[i[1]].append(i[0])
def bfs(x):
    cnt = 1
    queue = deque()
    queue.append(x)
    while(queue):
        x = queue.popleft()
        for i in edge[x]:
            if visited[i] == 0:
                cnt += 1
                queue.append(i)
                visited[i] = 1
    return cnt
ans_cnt = 0
ans = []
for i in range(1, n+1):
    visited = [0] * (n+1)
    temp = bfs(i)
    if temp > ans_cnt:
        ans_cnt = temp
        ans = [i]
    elif temp == ans_cnt:
        ans_cnt = temp
        ans.append(i)
ans.sort()
print(*ans)
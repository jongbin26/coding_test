t = int(input())
ans = []

def dfs(i):
    if not visited[arr[i]]:
        visited[arr[i]] = 1
        dfs(arr[i])

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    ans.append(cnt)
for i in ans:
    print(i)
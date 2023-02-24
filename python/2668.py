n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
def dfs(num):
    if visited[num] == False:
        visited[num] = True
        first.add(num)
        second.add(arr[num])
        if first == second:
            for i in second:
                ans.append(i)
            return
        dfs(arr[num])
    visited[num] = False
ans = []
for i in range(1, n+1):
    visited = [False] * (n+1)
    first, second = set(), set()
    dfs(i)
ans = list(set(ans))
ans.sort()
print(len(ans))
for i in ans:
    print(i)
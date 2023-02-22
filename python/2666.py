n = int(input())
open_door = list(map(int, input().split()))
m = int(input())
order = [int(input()) for _ in range(m)]
ans = int(1e9)
def dfs(depth, x, open_door, move):
    global ans
    if depth == m-1:
        if move+abs(x-open_door[0]) < move+abs(x-open_door[1]):
            ans = min(ans, move+abs(x-open_door[0]))
        else:
            ans = min(ans, move+abs(x-open_door[1]))
        return
    dfs(depth+1, order[depth+1], [x, open_door[1]], move+abs(x-open_door[0]))
    dfs(depth+1, order[depth+1], [open_door[0], x], move+abs(x-open_door[1]))
dfs(0, order[0], open_door, 0)
print(ans)
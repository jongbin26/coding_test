import sys
# sys.setrecursionlimit(10 ** 8)

n = int(input())
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int,input().split()))
rd = {}
for i in range(-n+1, n):
    rd[i] = 0
def upper_bound(diag):
    cnt = 0
    for d in range(diag, 2 * n - 1):
        for y in range(d+1):
            x = d - y
            if 0 <= x < n and 0 <= y < n:
                if board[y][x] and not rd[x - y]:
                    cnt += 1
                    break
    return cnt

def bishop(diag, cnt):
    global ans 
    if diag == 2 * n:
        ans = max(ans, cnt)
        return
    ub = upper_bound(diag)
    if ub + cnt <= ans:
        return
    for y in range(diag+1):
        x = diag - y
        if 0 <= x < n and 0 <= y < n:
            if board[y][x] and not rd[x - y]:
                rd[x-y] = 1
                bishop(diag+1, cnt+1)
                rd[x-y] = 0
    bishop(diag+1, cnt)
ans = 0
bishop(0,0)
print(ans)
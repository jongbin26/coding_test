n, x, y = map(int, input().split())
space = abs(x - y) - 1
sequence = [0] * (2*n + 1)
sequence[x] = sequence[y] = space

def langford(sequence):
    for i in range(1, len(sequence)):
        if not sequence[i]:
            return False
    return True

def dfs(n, sequence):
    global ans
    #이미 처음에 넣었던 수는 건너뛰기
    if n == space:
        dfs(n+1, sequence)
        return
    #꽉 찼을 때 랭포드 검사
    if n == len(sequence)//2 +1 and langford(sequence):
        ans += 1
        return
    for i in range(1, len(sequence)):
        if not sequence[i]:
            if i + n + 1 < len(sequence) and not sequence[i+n+1]:
                sequence[i] = n
                sequence[i + n + 1] = n
                dfs(n+1, sequence)
                sequence[i] = 0
                sequence[i + n + 1] = 0
ans = 0
dfs(1, sequence)
print(ans)
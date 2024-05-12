board = []
ans = 1e9
for i in range(10):
    temp = list(input())
    for j in range(10):
        if temp[j] == 'O':
            temp[j] = 1
        else:
            temp[j] = 0
    board.append(temp)
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
for f in range(1<<10):
    check = []
    for i in range(10):
        check.append(board[i][:])
    cnt = 0
    for i in range(10):
        if f & (1<<i):
            cnt += 1
            for k in range(5):
                nx = i + dx[k]
                ny = dy[k]
                if 0 <= nx < 10 and 0 <= ny < 10:
                    check[ny][nx] = not check[ny][nx]
    for i in range(1, 10):
        for j in range(10):
            if not check[i-1][j]:
                continue
            for k in range(5):
                nx = j + dx[k]
                ny = i + dy[k]
                if 0 <= nx < 10 and 0 <= ny < 10:
                    check[ny][nx] = not check[ny][nx]
            cnt += 1
    isOff = True
    for i in range(10):
        if check[9][i] == True:
            isOff = False
    if isOff:
        ans = min(cnt, ans)
print(ans if ans != 1e9 else -1)

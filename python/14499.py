n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
order = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]

def roll(direct, dice):
    if direct == 1:
        temp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp
        
    if direct == 2:
        temp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[2]
        dice[2] = temp
    if direct == 3:
        temp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp
    if direct == 4:
        temp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp
        
for i in order:
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
        x = nx
        y = ny
        roll(i, dice)
        if graph[x][y] == 0:
            graph[x][y] = dice[5]
        else:
            dice[5] = graph[x][y]
            graph[x][y] = 0
        print(dice[0])
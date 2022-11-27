n = int(input())
balloon = list(map(int, input().split()))

ans = 0
for i in range(len(balloon)):
    if balloon[i] > 0:
        ans += 1
        y = balloon[i] - 1
        for x in range(i+1, len(balloon)):
            if y == 0:
                break
            if balloon[x] == y:
                y -= 1
                balloon[x] = 0
            
print(ans)
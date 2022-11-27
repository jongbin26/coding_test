n = int(input())
balloon = list(map(int, input().split()))
arrow = [0] * (n+1)
ans = 0
for i in range(n):
    height = balloon[i]
    if arrow[height]:
        arrow[height] -=1
        arrow[height-1] += 1
    else:
        ans += 1
        arrow[height-1]+= 1
print(ans)
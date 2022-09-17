N = int(input())
limit = list(map(int, input().split()))
M = int(input())
weight = list(map(int, input().split()))

limit.sort(reverse = True)
weight.sort(reverse = True)

ans = 0
while(weight):
    if limit[0] < weight[0]:
        print(-1)
        exit()
    for i in limit:
        for j in weight:
            if j <= i:
                weight.remove(j)
                break
    ans += 1
print(ans)


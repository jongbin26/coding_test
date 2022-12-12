import heapq
n, m = map(int, input().split())
time = list(map(int, input().split()))
q = []
for i in time:
    heapq.heappush(q, (-i, i))

ans = 0
concent_use = False

if m == 1:
    sum = 0
    for i in q:
        sum += i[1]
    print(sum)
    exit()
while(True):
    if q:
        if not concent_use:
            concent_use = True
            temp = heapq.heappop(q)
            ans += temp[1]
            concent_time = temp[1] * (m - 1)
        else:
            temp = heapq.heappop(q)
            concent_time -= temp[1]
            if concent_time <= 0:
                concent_use = False
    else:
        break
print(ans)
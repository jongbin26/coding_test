import heapq
plus = []
minus = []
n = int(input())
ans = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if not plus and not minus:
            ans.append(0)
        elif plus and not minus:
            ans.append(heapq.heappop(plus))
        elif not plus and minus:
            ans.append(heapq.heappop(minus)[1])
        else:
            if plus[0] < minus[0][0]:
                ans.append(heapq.heappop(plus))
            else:
                ans.append(heapq.heappop(minus)[1])
    else:
        if x > 0:
            heapq.heappush(plus, x)
        else:
            heapq.heappush(minus, [-x, x])
for i in ans:
    print(i)
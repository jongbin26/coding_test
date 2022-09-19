N, M = map(int, input().split())
dist = list(map(int, input().split()))
plus = []
minus = []
for i in dist:
    if i < 0 :
        minus.append(i)
    else:
        plus.append(i)
        
plus.sort(reverse = True)
minus.sort()
ans = 0

if not plus:
    for i in range(0, len(minus), M):
        ans += 2 * (abs(minus[i]))
    ans -= abs(minus[0])
    print(ans)
    exit()
if not minus:
    for i in range(0, len(plus), M):
        ans += 2 * (plus[i])
    ans -= plus[0]
    print(ans)
    exit()

if plus[0] < abs(minus[0]): #음수 절댓값 큰 경우
    for i in range(0, len(minus), M):
        ans += 2 * (abs(minus[i]))
    ans -= abs(minus[0]) #가장 큰 값 보정
    for j in range(0, len(plus), M):
        ans += 2 * (plus[j])
else:
    for i in range(0, len(plus), M):
        ans += 2 * (plus[i])
    ans -= plus[0] #가장 큰 값 보정
    for j in range(0, len(minus), M):
        ans += 2 * (abs(minus[j]))
print(ans)
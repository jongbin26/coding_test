a, b = map(int, input().split())
ans = 0
while(True):
    if b == a:
        ans += 1
        break
    if b < a:
        ans = -1
        break

    if (str(b)[-1] == '1'):
        b = int(str(b)[:-1])
        ans += 1
        continue
    elif b % 2 == 0:
        b //= 2
        ans += 1
        continue
    else:
        ans = -1
        break
print(ans)
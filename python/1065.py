n = int(input())
ans = 0
for i in range(1, n+1):
    hansu = True
    num = str(i)
    if len(num) > 1:
        temp = int(num[1]) - int(num[0])
        for j in range(1, len(num)):
            if int(num[j]) - int(num[j-1]) != temp:
                hansu = False
    if hansu: ans += 1
print(ans)
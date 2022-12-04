n = int(input())

ans = -1
def decrease(num, cnt):
    global ans
    if len(num) == cnt:
        ans += 1
        if ans == n:
            print(num)
            exit()
    else:
        if num == '':
            for i in range(cnt - 1, 10):
                decrease(str(i), cnt)
        else:
            for i in range(cnt - 1 - len(num), int(num[-1])):
                decrease(num + str(i), cnt)
            

for i in range(1, 11):
    decrease('', i)
print(-1)
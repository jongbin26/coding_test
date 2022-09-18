N = int(input())
work = [list(map(int, input().split())) for _ in range(N)]
work.sort(key = lambda a : -a[1])
day = [False]*1001

done = []
for i in work:
    for j in range(i[0], 0, -1):
        if day[j] == 0:
            day[j] = True
            done.append(i)
            break
sum = 0        
for i in done:
    sum += i[1]
print(sum)
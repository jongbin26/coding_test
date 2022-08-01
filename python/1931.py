time = []
n = int(input())
for _ in range(n):
    time.append(list(map(int, input().split())))

time=sorted(time, key=lambda a : a[0])
print(time)
time=sorted(time, key=lambda a : a[1])
print(time)
end = 0
ans = 0
for i in time:
    if end <= i[0]:
        end = i[1]
        ans += 1
print(ans)
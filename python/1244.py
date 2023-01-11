n = int(input())
switch = list(map(int, input().split()))
k = int(input())
arr = [list(map(int, input().split())) for _ in range(k)]

def man(x):
    for i in range(n):
        if (i+1) % x == 0:
            switch[i] = not switch[i]
def woman(x):
    switch[x-1] = not switch[x-1]
    left, right = x-2, x
    while(left >= 0 and right < n):
        if switch[left] == switch[right]:
            switch[left] = not switch[left]
            switch[right] = not switch[right]
            left, right = left-1, right+1
        else:
            break

for i in arr:
    if i[0] == 1:
        man(i[1])
    else:
        woman(i[1])

ans = ''
cnt = 0
for i in switch:
    if i:
        ans += '1 '
    else:
        ans += '0 '
    cnt += 1
    if cnt == 20:
        print(ans[:-1])
        ans = ''
        cnt = 0
ans = ''
if ans:
    print(ans[:-1])
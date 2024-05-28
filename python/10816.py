n = int(input())
arr = list(map(int, input().split()))
cnt = {}
for i in arr:
    if not cnt.get(i):
        cnt[i] = 1
    else: cnt[i] += 1
m = int(input())
key = list(map(int, input().split()))
for i in key:
    if cnt.get(i):
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')
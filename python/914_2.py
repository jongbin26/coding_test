n, d = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

num = [0] * 300001
max_num = arr[0]
for i in arr:
    num[i] += 1

ans = 0
for i in range(max_num, max_num-d,-1):
    if i == 0:
        print(0)
        exit()
    ans += num[i]
    if i-1 > 0:
        num[i-1] += num[i]
    else:
        break
print(ans)
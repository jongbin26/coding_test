T = int(input())
ans = []
arr = [0] * 101
arr[1], arr[2], arr[3] = 1, 1, 1

for i in range(4, 101):
    arr[i] = arr[i-2] + arr[i-3]
for _ in range(T):
    N = int(input())
    ans.append(arr[N])

for i in ans:
    print(i)
    
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    high = arr[n-1]
    total = 0
    for i in range(n-2, -1, -1):
        if arr[i] <= high:
            total += high - arr[i]
        else:
            high = arr[i]
    ans.append(total)
for i in ans:
    print(i)
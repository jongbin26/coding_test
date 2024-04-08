n = int(input())
ans = []
for _ in range(n):
    a, b = map(int, input().split())
    while(True):
        if a == b:
            ans.append(a * 10)
            break
        if a > b:
            a //= 2
        else:
            b //= 2
for i in ans:
    print(i)
from itertools import combinations_with_replacement
n, m = map(int, input().split())
num = list(map(int, input().split()))
num = list(set(num))
num.sort()

ans = list(combinations_with_replacement(num, m))
for i in ans:
    for j in i:
        print(j, end=" ")
    print()
import itertools
n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    temp = list(itertools.combinations(arr, i))
    for j in temp:
        if sum(j) == s: ans+=1
print(ans)

def combination(arr , n):
    temp = []
    if n > len(arr): return temp
    if n ==1 :
        for i in arr: temp.append(i)
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in combination(arr[i+1:], n-1):
                temp.append([arr[i]] + j)
    return temp
print(combination(arr, 4))
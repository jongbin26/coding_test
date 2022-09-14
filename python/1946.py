n = int(input())
ans = []
for _ in range(n):
    num = int(input())
    rank = []
    for _ in range(num):
        rank.append(list(map(int, input().split())))
    rank.sort()
    least = rank[0][1]
    for i in range(1, num):
        if rank[i][1] > least:
            num -= 1
        else:
            least = rank[i][1]
    ans.append(num)
    
for i in ans:
    print(i)
n = int(input())
consult = [list(map(int, input().split())) for _ in range(n)]
temp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if i + consult[i][0] <= n:
        temp[i] = max(temp[i+1], temp[i + consult[i][0]] + consult[i][1])
    else:
        temp[i] = temp[i+1]
        
print(temp[0])
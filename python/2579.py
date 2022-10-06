n = int(input())
score = [0]
for _ in range(n):
    score.append(int(input()))
rank = [0] * (n+1)

if n == 1:
    print(score[1])
    exit()
rank[1] = score[1]
rank[2] = score[1] + score[2]
for i in range(3, n+1):
    rank[i] = max(rank[i-2]+score[i] , rank[i-3]+score[i-1]+score[i])
    
print(rank[n])
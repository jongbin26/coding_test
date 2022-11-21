n, k = map(int, input().split())
height = list(map(int, input().split()))
cost = []
for i in range(0, len(height)-1):
    cost.append(height[i+1] - height[i])
cost.sort()
print(sum(cost[:n-k]))
n = int(input())
line = list(map(int, input().split()))
price = list(map(int, input().split()))

total = [[0] * 2 for _ in range(n)] 
total[1] = [line[0] * price[0], price[0]]
for i in range(2, n):
    if total[i-1][1] * line[i-1] <= price[i-1] * line[i-1]:
        total[i] = [total[i-1][0] + total[i-1][1] * line[i-1], total[i-1][1]]
    else:
        total[i] = [total[i-1][0] + price[i-1] * line[i-1], price[i-1]]
        
print(total[n-1][0])
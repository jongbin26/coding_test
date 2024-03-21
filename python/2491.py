n = int(input())
data = list(map(int, input().split()))
inc = [0] * (n)
dec = [0] * (n)
inc[0], dec[0] = 1, 1
for i in range(1, n):
    if data[i] <= data[i-1]:
        dec[i] = dec[i-1]+1
    else:
        dec[i] = 1

    if data[i] >= data[i-1]:
        inc[i] = inc[i-1]+1
    else:
        inc[i] = 1
print(max(max(inc), max(dec)))
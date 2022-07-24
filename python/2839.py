n = int(input())

def sugar(n):
    sum = 0
    while(n >= 0):
        if n % 5 == 0:
            sum += n // 5
            return sum
        n -= 3
        sum += 1
    return(-1)

print(sugar(n))
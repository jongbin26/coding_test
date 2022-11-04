def recursivePower(a, n):
    if n == 1:
        return a % c
    if n % 2 == 0:
        divide = recursivePower(a, n/2)
        return (divide * divide) % c
    else:
        divide = recursivePower(a, (n-1)/2)
        return (divide * divide * a) % c
    
a, b, c = map(int, input().split())
print(recursivePower(a, b))
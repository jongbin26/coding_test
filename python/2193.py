n = int(input())
arr = [0] * (n+1)
if n == 1:
    print(1)
    exit()

arr[1] = 1
arr[2] = 1
for i in range(3, n+1):
    arr[i] = arr[i-1] + arr[i-2]
    
print(arr[n])
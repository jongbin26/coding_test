n = int(input())
data = list(map(int, input().split()))
data.sort()
ans, arr = float('inf'), []

for i in range(n-2):
    left, right = i+1, n-1
    while(left < right):
        temp = data[i] + data[left] + data[right]
        if(abs(temp) < ans):
            ans = abs(temp)
            arr = [data[i], data[left], data[right]]
        if(temp < 0):
            left += 1
        else:
            right -= 1
print(arr[0], arr[1], arr[2])

left, right = 0, n-1
while(left < right):
    for mid in range(left+1, right):
        temp = data[left] + data[mid] + data[right]
        if(abs(temp) < ans):
            ans = abs(temp)
            arr = [data[left], data[mid], data[right]]
    if(abs(data[left+1] + data[right]) < abs(data[left] + data[right-1])):
        left += 1
    else:
        right -= 1
print(arr[0], arr[1], arr[2])
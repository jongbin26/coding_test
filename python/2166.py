n = int(input())
x_arr, y_arr = [], []
for _ in range(n):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)
x_arr.append(x_arr[0])
y_arr.append(y_arr[0])
left, right = 0, 0
for i in range(n):
    left += x_arr[i]*y_arr[i+1]
    right += x_arr[i+1]*y_arr[i]
print(abs(left-right)/2)
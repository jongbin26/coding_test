from collections import deque
n = int(input())

minus = []
zero = []
plus = []
for _ in range(n):
    temp = int(input())
    if temp > 0:
        plus.append(temp)
    elif temp < 0:
        minus.append(temp)
    else:
        zero.append(temp)
plus.sort()
minus.sort()

def plus_calc():
    if len(plus) % 2 == 0:
        even_calc(plus)
    else:
        odd_calc(plus)
        
def odd_calc(arr):
    global ans
    if arr:
        if arr[0] > 0:
            while(len(arr) != 1):
                a = arr.pop()
                b = arr.pop()
                if a == 1 or b == 1:
                    ans += a + b
                else:
                    ans += a * b
            ans += arr.pop()
        else:
            while(len(arr) != 1):
                a = arr.pop(0)
                b = arr.pop(0)
                ans += a * b
            ans += arr.pop()
    
def even_calc(arr):
    global ans
    if arr:
        if arr[0] > 0:
            while(arr):
                a = arr.pop()
                b = arr.pop()
                if a == 1 or b == 1:
                    ans += a + b
                else:
                    ans += a * b
        else:
            while(arr):
                a = arr.pop()
                b = arr.pop()
                ans += a * b
ans = 0
if len(minus) % 2 == 0:
    even_calc(minus)
    plus_calc()
else:
    if zero:
        minus.pop()
        even_calc(minus)
        plus_calc()
    else:
        odd_calc(minus)
        plus_calc()
print(ans)
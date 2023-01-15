arr = [0, 0, 0, 0 ,0, 0]
for i in range(6):
    inp = int(input())
    for j in range(inp):
        arr[i] += ((i+1)*(i+1))

cnt = 0
while 1:
    if max(arr) == 0:
        break
    result = 36
    
    if arr[5] >= 36:
        cnt += 1
        arr[5] -= 36
        continue
        
    elif arr[4] >= 25:
        arr[4] -= 25
        cnt += 1
        for i in range(11):
            if arr[0] == 0:
                break
            arr[0] -= 1
        continue
            
    elif arr[3] >= 16:
        arr[3] -= 16
        cnt += 1
        result -= 16
        for i in range(5):
            if arr[1] == 0:
                break
            arr[1] -= 4
            result -= 4
        for i in range(20):
            if arr[0] == 0 or result == 0:
                break
            arr[0] -= 1
            result -= 1
        continue
        
    elif arr[2] >= 9:
        if arr[2] >= 36:
            arr[2] -= 36
            result -= 36
            cnt += 1
        elif arr[2] >= 27:
            cnt += 1
            arr[2] -= 27
            result -= 27
            if arr[1] >= 4:
                arr[1] -=4
                result -= 4
        elif arr[2] >= 18:
            cnt += 1
            arr[2] -= 18
            result -= 18
            for i in range(3):
                if arr[1] == 0 or result == 0:
                    break
                arr[1] -= 4
                result -= 4
        elif arr[2] >= 9:
            cnt += 1
            arr[2] -= 9
            result -= 9
            for i in range(5):
                if arr[1] == 0 or result == 0:
                    break
                arr[1] -=4
                result -= 4
        while 1:
            if arr[0] == 0  or result == 0:
                break
            arr[0] -= 1
            result -= 1
        continue
        
    elif arr[1] >= 4:
        cnt += 1
        for i in range(9):
            if arr[1] == 0:
                break
            result -= 4
            arr[1] -= 4
        while 1:
            if arr[0] == 0 or result == 0:
                break
            arr[0] -= 1
            result -= 1
        continue
        
    elif arr[0] >= 1:
        cnt += 1
        for i in range(36):
            if arr[0] == 0 or result == 0:
                break
            arr[0] -= 1
            result -= 1
        continue
print(cnt)
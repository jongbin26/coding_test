from collections import deque
T = int(input())
ans = []

def listify(string):
    if string == "[]":
        return []
    queue = deque()
    arr = []
    string = string.replace("[", "")
    string = string.replace("]", "")
    string += ","
    for i in string:
        if i != ",":
            queue.append(i)
        else:
            num = ""
            while(queue):
                num= num + (queue.popleft())
            arr.append(int(num))
    return arr

def stringify(queue, direction):
    temp = "["
    if direction:
        for i in queue:
            temp += str(i)
            temp += ','
    else:
        for i in range(len(queue)-1, -1, -1):
            temp += str(queue[i])
            temp += ','
    temp = temp[:-1]
    temp += "]"
    return temp

for _ in range(T):
    nums = []
    p = input()
    n = int(input())
    arr = listify(input())
    queue = deque(arr)
    
    direction = True
    error_bool = False
    for i in p:
        if i =="R":
            direction = not direction
        elif i == "D":
            if len(queue) > 0:
                if direction:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                ans.append("error")
                error_bool = True
                break
    if error_bool:
        continue
    else:
        if len(queue) > 0:
            ans.append(stringify(queue, direction))
        elif len(queue) == 0:
            ans.append("[]")
            
    
for i in ans:
    print(i)
                
    
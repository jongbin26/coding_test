string = input()
bomb = input()

stack = []

i = 0
while(i < len(string)):
    stack.append(string[i])
    if stack[len(stack)-1] == bomb[-1]:
        if (i+1) - len(bomb) >= 0:
            if ''.join(stack[-len(bomb):]) == bomb:
                for _ in range(len(bomb)):
                    stack.pop()
    i += 1

if stack:
    print(''.join(stack))
else:
    print("FRULA")
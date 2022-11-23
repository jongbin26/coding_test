string = input()
stack = []
i = 0

if len(string) < 4:
    if string == 'P':
        print("PPAP")
    else:
        print("NP")
    exit()

while(i < len(string)):
    stack.append(string[i])
    if stack[len(stack)-1] == 'A':
        if len(stack) > 2 and i+1 < len(string):
            if stack[len(stack)-2] == 'P' and stack[len(stack)-3] == 'P' and string[i+1] == 'P':
                for _ in range(3):
                    stack.pop()
            stack.append(string[i+1])
            i += 1
    i += 1
    
if len(stack) == 1:
    if stack[0] == 'P':
        print("PPAP")
else:
    print("NP")
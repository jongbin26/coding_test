n = int(input())
line = []
stack = []

def push(stack, x):
    stack.append(x)
    
def pop(stack):
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def size(stack):
    return len(stack)

def empty(stack):
    if not stack:
        return 1
    else:
        return 0
def top(stack):
    if len(stack) == 0:
        return -1
    else:
        return stack[len(stack)-1]

for _ in range(n):
    line.append(list(map(str, input().split())))

for i in range(n):
    if len(line[i]) != 1:
        push(stack, line[i][1])
    else:
        if line[i][0] == 'pop':
            print(pop(stack))
        elif line[i][0] == 'size':
            print(size(stack))
        elif line[i][0] == 'empty':
            print(empty(stack))
        elif line[i][0] == 'top':
            print(top(stack))
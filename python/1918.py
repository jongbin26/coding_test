before = list(input())
stack = []
after = ''
oper = ['+', '-', '*', '/', '(', ')']
for i in before:
    if i not in oper:
        after += i
    else:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while(stack and stack[-1] != '('):
                after += stack.pop()
            stack.pop()
        elif i == '+' or i == '-':
            while(stack and stack[-1] != '('):
                  after += stack.pop()
            stack.append(i)
        elif i == '*' or i == '/':
            while(stack and (stack[-1] == '*' or stack[-1] == '/')):
                  after += stack.pop()
            stack.append(i)
while(stack):
    after += stack.pop()
print(after)
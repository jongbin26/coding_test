string = list(input())
def test(s):
    stack = []
    ans, temp = 0, 1
    for c in s:
        if c == '(':
            plus_bool = True
            temp *= 2
            stack.append(c)
        elif c == '[':
            plus_bool = True
            temp *= 3
            stack.append(c)
        else:
            if stack:
                pop = stack.pop()
                if pop == '(' and c == ')':
                    if plus_bool:
                        ans += temp
                        plus_bool = False
                    temp //= 2
                elif pop == '[' and c == ']':
                    if plus_bool:
                        ans += temp
                        plus_bool = False
                    temp //= 3
                else:
                    return 0
            else:
                return 0
    if stack:
        return 0
    else:
        return ans
print(test(string))
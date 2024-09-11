from itertools import combinations

exp = list(input())
exponent = []
stack = []
answers = set()

for i in range(len(exp)):
    if exp[i] == '(':
        stack.append(i)
    elif exp[i] == ')':
        exponent.append((stack.pop(), i))
for i in range(len(exponent)):
    for comb in combinations(exponent, i+1):
        temp = exp[:]
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = ""
        answers.add("".join(temp))      

for item in sorted(list(answers)):
    print(item)
n = int(input())
strings = [input() for _ in range(n)]

def test(string):
    if string == string[::-1]:
        return 0
    left, right = 0, len(string)-1
    while left <= right:
        if string[left] == string[right]:
            left, right = left+1, right-1
        else:
            pseudo_palindrome = False
            if string[left+1] == string[right]:
                string_temp = string[left+1:right+1]
                if string_temp == string_temp[::-1]:
                    pseudo_palindrome = True
            if string[right-1] == string[left]:
                string_temp = string[left:right]
                if string_temp == string_temp[::-1]:
                    pseudo_palindrome = True
            if pseudo_palindrome:
                return 1
            else:
                return 2
ans = []
for string in strings:
    print(test(string))
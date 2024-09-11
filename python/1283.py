n = int(input())
line = [input() for _ in range(n)]

def is_alpha(x):
    return x.isalpha()

alpha = [0] * 26

for string_idx, string in enumerate(line):
    words = string.split()
    shortcut_found = False
    
    # 각 단어의 첫 글자 확인
    for idx, word in enumerate(words):
        if word and is_alpha(word[0]):
            lower_char = word[0].lower()
            if not alpha[ord(lower_char) - ord('a')]:
                alpha[ord(lower_char) - ord('a')] = 1
                words[idx] = '[' + word[0] + ']' + word[1:]
                line[string_idx] = ' '.join(words)
                shortcut_found = True
                break
    
    # 첫 글자로 단축키를 찾지 못한 경우, 모든 글자 확인
    if not shortcut_found:
        for idx, char in enumerate(string):
            if is_alpha(char):
                lower_char = char.lower()
                if not alpha[ord(lower_char) - ord('a')]:
                    alpha[ord(lower_char) - ord('a')] = 1
                    string = string[:idx] + '[' + char + ']' + string[idx+1:]
                    line[string_idx] = string
                    break

for i in line:
    print(i)
a, b = map(str, input().split())

def sangsu(a, b):
    rev_a = ''.join(reversed(a))
    rev_b = ''.join(reversed(b))
    
    if rev_a > rev_b:
        return rev_a
    else:
        return rev_b
    
print(sangsu(a,b))
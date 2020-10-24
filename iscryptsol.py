def isCryptSolution(crypt, solution):
    a = crypt[0]
    b = crypt[1]
    c = crypt[2]
    
    ch = {}
    
    for i in solution:
        ch[i[0]] = int(i[1])
        
    hasLeadingzero = False
    
    if ch[a[0]] == 0 or ch[b[0]] == 0 or ch[c[0]] == 0:
        hasLeadingzero = True
        
    n1 = ''.join(str(ch[i]) for i in a)
    n2 = ''.join(str(ch[i]) for i in b)
    n3 = ''.join(str(ch[i]) for i in c)
    
    if int(n1) + int(n2) == int(n3):
        if hasLeadingzero and int(n3) == 0 and len(n3) == len(str(int(n3))):
            return True
        elif hasLeadingzero:
            return False
        else:
            return True
    else:
        return False

# 24/10/20
s = input()
if len(s)%2!=0:
    print(0)
else:
    sym = 0
    while len(s)>1:
        if s[0:len(s)//2]==s[len(s)//2:]:
            sym = sym + 1
            s = s[0:len(s)//2]
        else:
            break
    print(sym)

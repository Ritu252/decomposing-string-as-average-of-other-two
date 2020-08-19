n = int(input())
s = input()
def binaryToDecimal(num):
    d,i = 0,0
    while (num!=0):
        dec = num%10
        d = d + dec*pow(2,i)
        num = num//10
        i+=1
    return d
sum = binaryToDecimal(int(s))
def decimalToBinary(num):
    l = []
    while (num!=0):
        l.append(str(num%2))
        num = num//2
    l.reverse()
    return "".join(l)
for x in range(2*sum+1):
    for y in range(2*sum+1):
        if (x+y)==2*sum:
            p = str(decimalToBinary(x))
            q = str(decimalToBinary(y))
            if len(p)==n and len(q)==n:
                print(p,q)
                

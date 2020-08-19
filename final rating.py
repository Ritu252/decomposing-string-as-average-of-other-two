n = input().split()
r = int(n[1])
x = int(n[2])
y = int(n[3])
c = input().split()
s = input().split()
R = r
for i in range(len(c)):
    if s[i]=="1" and c[i]=="1":
        R+=x
    if c[i]=="1" and s[i]=="0":
        R-=y
if R>r:
   print("promoted")
elif R<r:
   print("demoted")
else:
   print("no change")

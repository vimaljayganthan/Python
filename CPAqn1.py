a=int(input())
s=input().split()

a=0
l=0
ac=0
lc=0

for i in range(a):
  if s[i]=="A":
    a+=1
    l=0
  elif s[i]=="L":
    l+=1
    a=0
  else:
    ac=0
    lc=0
  if a==2:
    ac=1
  if l==2:
    lc=1
  
if (ac==1) and (lc==1):
    print("Critical")
elif ac==2:
    print("ABSENCE WARNING")
elif lc==3:
    print("LATE WARNING")
else:
    print("GOOD")

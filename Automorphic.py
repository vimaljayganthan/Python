a=int(input())
org=a
count=0
while(a!=0):
  count+=1
  a//=10
square=org*org
print(square)
mul=1
while(count!=0):
  mul*=10
  count-=1
check=square%mul
print(check)
if(check==org):
  print("Automorphic")
else:
  print("Not Automorphic")
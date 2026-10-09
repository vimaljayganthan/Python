a=int(input())
v=1
for i in range(a):
  for j in range(i+1):
    print(v,end=" ")
    v+=1
  print()
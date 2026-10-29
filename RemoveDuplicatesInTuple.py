a=(1,1,1,2,2,2,3,3,3,4,5,4)
# a=set(a)
# print(tuple(a))

b=()
for i in a:
  if i not in b:
    b=b+(i,)
print(b)

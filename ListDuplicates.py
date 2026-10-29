list=[1,2,3,0,0,5,6,7]
result=[]
for i in list:
  if i not in result:
    result.append(i)
print(result)
sum=0
for i in result:
  sum+=i
print(sum)

a=input()
i=0

while i<len(a):
  count=0
  j=0
  while j<len(a):
    if a[i]==a[j]:
      count+=1
    j+=1

  print(a[i],count)
  i+=1
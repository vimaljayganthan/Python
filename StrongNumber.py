a = int(input())
temp = a
sum = 0
while(temp!=0):
  digit  = temp%10
  i = 1
  fact = 1
  temp = temp//10
  for i in range(1,digit+1):
    fact *= i
  sum += fact 
if(sum==a):
  print("Strong Number")
else:
  print("Not Strong Number")

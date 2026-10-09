x = int(input("Enter Units: "))
if(x>=0 and x<=100):
  print("Free")
elif(x>100 and x<=200):
  print((100)*10)
elif(x>200 and x<=300):
  print(((100)*10) + (x-200)*20)
elif(x>300 and x<=400):
  print(((100)*10) + (x-200)*20 + (x-300)*30)
elif(x>400 and x<=500):
  print(((100)*10) + (x-200)*20 + (x-300)*30 + (x-400)*40)
else:
  print(((100)*10) + (x-200)*20 + (x-300)*30 + (x-400)*40 + (x-500)*50)

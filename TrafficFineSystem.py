Speed = int(input())
Zone = input()
Fine = 0

if(0<= Speed <=60):
  Fine = 0
elif(60< Speed <=80):
  Fine = 1000
elif(80< Speed <=100):
  Fine = 2000
else:
  Fine = 5000

if(Zone == "No"):
  print(Fine)
else:
  print(Fine*2)
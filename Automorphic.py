a = int(input())
sq = a * a
div = 1
temp = a
while(temp != 0):
 temp = temp // 10
 div = div * 10
print(sq % div == a)
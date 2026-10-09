A={1,2}
B={2,3}
U={1,2,3,4,5,6,7,8,9}

V=U-(A|B)

W=U-A
X=U-B
Y=W&X
print("De-Morgan's Law is Satisfied") if V==Y else print("De-Morgan's Law is not Satisfied")

T=U-(A&B)
C=U|X
print("De-Morgan's Law is Satisfied") if T==C else print("De-Morgan's Law is not Satisfied")

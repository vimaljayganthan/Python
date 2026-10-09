A={1,2}
B={2,3}
C={3,4}

X=B|C
Y=A&X

U=A&B
V=A&C
W=U|V

print("Distributive property Satisfied") if Y==W else print("Distributive property not Satisfied")
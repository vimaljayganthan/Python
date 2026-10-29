A={1,2}
B={2,3}
C={3,4}

X=B&C
Y=A-X

W=A-B
T=A-C
Z=W&T

print("Property Satisfied") if Y==Z else print("Property Not Satisfied")

D=B|C
F=A-D
E=W|T

print("Property Satisfied") if F==E else print("Property Not Satisfied")


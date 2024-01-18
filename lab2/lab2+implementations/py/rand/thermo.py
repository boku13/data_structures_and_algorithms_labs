a = 0.422546
b = 37*(10**-6)

R = 8.314 
T = 321.55
p = 1.95*(10**6)

V_0 = b
print(V_0)

for i in range(8):
    v = (R*T)/(p+a/(V_0**2)) + b
    V_0 = v
    print(f'Volume in interation {i+1} is: {v}')
    
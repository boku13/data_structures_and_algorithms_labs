a = 0.422546
b = 37*(10**-6)
n=  1373/17
R = 8.314 
V = 0.1
p = 1.95*(10**6)

T = ((p+((a*(n**2))/V**2))*(V-n*b))/(R*n)
print(T)
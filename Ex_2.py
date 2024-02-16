import math
x=float(input("Enter the number: "))
s=math.sqrt(x)
z=x/2
while True:
    z1=(z+x/z)/2.0
    if abs(z-z1)<0.000001:
        break
    z=z1        
    
print("The Programs estimate: ",z)
print("Python's estimate: ",s)

a = int(input())
b = int(input())
c = int(input())

real = -b / (2*a)
imaginary = ((b**2 - 4*a*c)**0.5)/(2*a)

print(real + str(imaginary).replace('j','i'))
print(real - str(imaginary).replace('j','i'))
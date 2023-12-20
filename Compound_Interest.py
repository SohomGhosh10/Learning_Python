p = 10000
r = 12/100
n = 4
t = 4

res = p / ((1 + (r / n))**(n*t)) # for calculating compound interest
print(res)
print("%.2f" %res)

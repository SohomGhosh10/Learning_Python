n = 13
prime = 1

for i in range(2 , n-1):
    if n % i == 0:
        prime = 0
        break
if prime == 0:
    print("Not prime")
else:
    print("Prime")
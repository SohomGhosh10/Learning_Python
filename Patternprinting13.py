height = 5
for i in range(height , 0 , -1):
    for j in range(height , i - 1, -1):
        print(chr(i + 64) , end='')
    print()
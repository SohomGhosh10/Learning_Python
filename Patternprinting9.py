height = 4
for row in range(1 , height + 1):
    for col in range(height , 0 , -1):
        print(chr(col + 64) , end='')
    print()
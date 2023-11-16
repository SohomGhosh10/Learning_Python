h = int(input())
for row in range(1 , h + 1 , 1):
    for spaces in range(1 , h - row + 1):
        print(' ',end='')
    for col in range(1 , row + 1):
        print(row , end='')
    print()
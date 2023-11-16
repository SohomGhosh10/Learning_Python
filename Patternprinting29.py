h = int(input())
for row in range(h , 0 , -1):
    for spaces in range(1 , row  , 1):
        print(' ',end='')
    for col in range(h , row - 1, -1):
        print(col , end='')
    print()
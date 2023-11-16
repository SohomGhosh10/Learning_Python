h = int(input())
for row in range(1 , h + 1 , 1):
    for col in range(h , row - 1 , -1):
        print(chr(col + 64) , end='')
    print()
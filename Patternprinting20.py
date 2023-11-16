h = int(input())
for row in range(h , 0 , -1):
    for col in range(1 , row + 1 , 1):
        print(row , end='')
    print()
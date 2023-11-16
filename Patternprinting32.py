height = 4
for row in range(1 , height + 1):
    for space in range(1 , row - 1 + 1):
        print(end='')
    for col in range(height , row - 1 , -1):
        print(row , end='')
    print()
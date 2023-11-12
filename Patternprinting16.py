height = 5
for row in range(1 , height + 1):
    for j in range(height , row - 1 , -1):
        print(row , end='')
    print()
    
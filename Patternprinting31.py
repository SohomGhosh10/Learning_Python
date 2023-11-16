rows = 5  # Adjust the number of rows as needed

for i in range(rows, 0, -1):
    # Add spaces before the numbers in each row
    for j in range(rows - i):
        print(" ",end="")

    # Print the numbers for the current row
    for k in range(1, i + 1):
        print(k, end="")

    # Move to the next line after each row
    print()
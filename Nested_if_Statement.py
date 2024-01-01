age = int(input())
if age < 60: #1st if
    if age < 18: # Nested if
        print("Minor")
    else:
        print("adult")
else:
    print("Senior citizen")

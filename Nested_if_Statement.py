age = int(input())
if age < 60:
    if age < 18:
        print("Minor")
    else:
        print("adult")
else:
    print("Senior citizen")
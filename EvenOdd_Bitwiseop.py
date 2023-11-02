def is_even_or_odd(number):
    if number & 1 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
num = 5
result = is_even_or_odd(num)
print(f"{num} is {result}")
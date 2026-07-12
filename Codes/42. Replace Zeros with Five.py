# replace zeros with five
n = int(input("Enter a number: "))
new_number = 0
place_value = 1
while n > 0:
    digit = n % 10
    if digit == 0:
        digit = 5
    new_number += digit * place_value
    place_value *= 10
    n //= 10
print("Number after replacing zeros with five:", new_number)
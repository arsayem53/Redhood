#smallest digit
n = int(input("Enter a number: "))
smallest_digit = 9
while n > 0:
    digit = n % 10
    if digit < smallest_digit:
        smallest_digit = digit
    n = n // 10
print("Smallest digit in the number is:", smallest_digit)
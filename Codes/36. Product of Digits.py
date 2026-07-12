#product of digits
n = int(input("Enter a number: "))
product_of_digits = 1
while n > 0:
    digit = n % 10
    product_of_digits *= digit
    n = n // 10
print("Product of digits in the number is:", product_of_digits)

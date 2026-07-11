#program to read two numbers and print their sum, difference, product and quotient.
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
sum = num1 + num2
diff = abs(num1 - num2)
product = num1 * num2
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "undefined (division by zero)"

print(f"Sum: {sum}")
print(f"Difference: {diff}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
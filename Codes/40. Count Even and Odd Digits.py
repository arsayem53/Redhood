# count even and odd digits
n = int(input("Enter a number: "))
odd = 0
even = 0
if n == 0:
    even += 1
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n // 10
print(f"Even number: {even}, Odd number: {odd}")

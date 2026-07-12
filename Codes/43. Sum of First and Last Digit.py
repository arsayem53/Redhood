# last + first digit sum
n = int(input("Enter number: "))
last = n % 10
n = n // 10
first = 0
sum = 0
if n == 0:
    first = last
    sum = last + first

while n > 0:
    digit = n % 10
    n = n // 10
    if n == 0:
        first = digit
sum = last + first
print(f"Sum: {sum}")


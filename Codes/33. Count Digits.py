#count digits in a number
n = int(input("Enter a number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print("Count of digits in the number is:", count)

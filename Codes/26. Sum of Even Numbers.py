#sum of even number
n = int(input("Enter a number:"))
sum = 0
for i in range(2, n + 1, 2):
    sum = sum + i
print("The sum of even numbers is:", sum)
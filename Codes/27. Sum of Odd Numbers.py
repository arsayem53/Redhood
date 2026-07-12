#sum of odd number
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1, 2):
    sum = sum + i
print("The sum of odd numbers is:", sum)
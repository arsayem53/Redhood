#palindrome
n = int(input("Enter number: "))
original = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Its a palindrome")
else:
    print("Its not a palindrome")

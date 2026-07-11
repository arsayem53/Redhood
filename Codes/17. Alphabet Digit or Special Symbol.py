#alphabet or digit or special symbol
target = input("Enter Char: ")
if target.isalpha():
    print("This is an alphabet")
elif target.isdigit():
    print("This is a digit")
else:
    print("This is a special symbol")

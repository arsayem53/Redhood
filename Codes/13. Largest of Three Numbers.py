#largest number
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))

max = num1

if max < num2:
       max = num2
       if max < num3:
          max = num3
       else:
          max = num2

elif max < num3:
       max = num3
else:
    max = num1

print("The largest number is", max)

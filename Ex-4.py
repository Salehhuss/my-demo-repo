# Exercise 4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

largest_number = num1
if num2 > largest_number:
    largest_number = num2
if num3 > largest_number:
    largest_number = num3
if num4 > largest_number:
    largest_number = num4

print("The largest number is:", largest_number)

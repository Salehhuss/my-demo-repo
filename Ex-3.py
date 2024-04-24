# Exercise 3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 == num2 == num3:
    print("4 times the sum of the numbers:", 4 * (num1 + num2 + num3))
else:
    print("Sum of the numbers:", num1 + num2 + num3)
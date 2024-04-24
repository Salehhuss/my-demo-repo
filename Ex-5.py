# Exercise 5
income = int(input("Enter your income: "))
if income < 67000:
    tax_rate = 0.24
elif income < 97000:
    tax_rate = 0.31
else:
    tax_rate = 0.34

taxes = income * tax_rate
net_income = income - taxes

print(f"Your income after taxes is {net_income} euros.")

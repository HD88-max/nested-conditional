#Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75

unit = int(input("How many units of electricity do you use per month? "))

if unit < 50:
    amount = unit*2.6
    tax = 25
elif unit <= 100:
    amount = 50*2.6 + (unit-50)*3.25
    tax = 35
elif unit <= 200:
    amount = 50*2.6 + 50*3.25 +(unit - 100)*5.26
    tax = 45
else:
    amount = 50*2.6 + 50*3.25 + 100*5.26 + (unit - 200)*8.45
    tax = 75

total = amount + tax
print("The toatal bill of electricity used is £{0}".format(total))
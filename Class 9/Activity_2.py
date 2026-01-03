# Electricity bill:

unit = int(input("How many units are being used?: "))

if unit < 50:
    price = unit * 2.60
    tax = 25

elif unit <= 100:
    price = 130 + ((unit - 50)*3.25)
    tax = 35

elif unit <= 200:
    price = 130 + 162.50 + ((unit - 100)*5.26)
    tax = 45

else:
    price = 130 + 162.50 + 526 + ((unit - 200)*8.45)
    tax = 75

amount = price + tax
print(amount)
original_price = int(input("Enter the original price of the product: "))
selling_price = int(input("Enter the selling price: "))

if original_price < selling_price:
    profit = (selling_price - original_price)
    print("The Profit it: ", profit)
else:
    print("No Profit")
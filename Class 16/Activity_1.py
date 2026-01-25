# Tip the waiter:

def total_value(bill_amount, tip_amount):
    total = bill_amount * (1 + 0.01*tip_amount)
    total = round(total, 2)
    print(f"Your grand total is ${total}")

total_value(150,20)
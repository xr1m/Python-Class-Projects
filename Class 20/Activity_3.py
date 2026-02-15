# Trip Expenditure:

def hotelcost(nights):
    return 140 * nights
def planecost(city):
    if "Delhi" == city:
        return 4000
    elif "Noida" == city:
        return 3500
    elif "Manipur" == city:
        return 6000
def rentingcar(days):
    if days > 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days
def tripcost(city, days, expense):
    return rentingcar(days) + planecost(city) + hotelcost(days) + expense
print("Cost of car rental =", rentingcar(8))
print("Cost of  plane trip =", planecost("Delhi"))
print("Cost of staying in hotel =", hotelcost(5))
print("Total trip cost:", tripcost("Delhi", 5, 7000))

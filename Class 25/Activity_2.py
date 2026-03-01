# Zip It!:

dict1 = {2, 3, 1}
dict2 = {'b', 'a', 'c'}
result_dict = list(zip(dict1, dict2))
print(result_dict)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)

stock = ["reliance", "infosys", "tcs"]
price = [500, 1000, 1500]
new_dict = {stock: price for stock, price in zip(stock, price)}
print("\n {}".format(new_dict))
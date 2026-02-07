# Trial and Error:

try:
    num1, num2 = eval(input("Enter any two numbers seperated by a comma: "))
    result = num1 / num2
    print(result)

except ZeroDivisionError:
    print(ZeroDivisionError)
except SyntaxError:
    print(SyntaxError)
except:
    print("Wrong Input.")
else:
    print("No exception.")
finally:
    print("This will print no matter what.")
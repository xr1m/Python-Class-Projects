# Get the country code:

country_code = {"india": "0091", "australia": "0025", "nepal": "00977"}
print("The country code for India is: ")
print(country_code.get("india", "not found"))
print(country_code.get("australia", "not found"))
print(country_code.get("nepal", "not found"))
print(country_code.get("japan", "not found"))
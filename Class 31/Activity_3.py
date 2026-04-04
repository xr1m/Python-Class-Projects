# All about Countries:

class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely used language in India.")
    def type(self):
        print("It is a developing country.")

print()

class USA():
    def capital(self):
        print("Washington D.C. is the capital of USA.")
    def language(self):
        print("English is the most widely used language in USA.")
    def type(self):
        print("It is a developed country.")

obj1 = India()
obj2 = USA()

for country in (obj1, obj2):
    country.capital()
    country.language()
    country.type()
    print("\n")
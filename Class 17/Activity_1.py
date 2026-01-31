# Break:

user_input = input("Enter any word: ")

for i in user_input:
    if i == 'A':
        print("A is found")
        break
    else:
        print("A is not found.")
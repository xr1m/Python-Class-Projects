# Reversing a word/sentence:

userinput = input("Enter your word to be reversed: ")
input2 = ('')

for i in userinput:
    input2 = i + input2

print(f"This is your original input: {userinput}")
print(f"This is your reveresed result: {input2}")
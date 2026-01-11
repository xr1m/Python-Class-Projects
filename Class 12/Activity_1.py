# Character occurrence:

string = input("Enter your text: ")
char = input("Enter the character of which you want to see the occurance: ")

i = 0
count = 0

while i < len(string):
    if string[i].lower() == char:
        count = count + 1
    i = i + 1
print(f"The number of times the {char} appeared in the text is: {count}")
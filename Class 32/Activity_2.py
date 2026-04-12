# Flashcards:

class flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + '('+self.meaning+')'
flash = []
print("Welcome to flashcards app.")

while(True):
    word = input("Enter your word to store in flashcard: ")
    meaning = input("Enter the meaning of the word: ")

    flash.append(flashcards(word, meaning))
    option = int(input("Enter 0 if you want to add more, else enter 1: "))
    if option:
        break
print("Your Flashcards:")
for i in flash:
    print(i)
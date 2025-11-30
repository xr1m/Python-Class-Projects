# Counting the notes:

amount = int(input("How much amount: "))
note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10
print("Notes of 100: ", note1)
print("Notes of 50: ", note2)
print("Notes of 10: ", note3)
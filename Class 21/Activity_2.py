# Word matching:

def matchedwords(words):
    count = 0
    list1 = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count = count + 1
            list1.append(word)
    print("List of words which have the same first and last character:", list1)
    return count

x = matchedwords(["abc", "cbc", "aba", "madam"])
print("Number of words having first and last letter same:", x)
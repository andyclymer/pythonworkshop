import random

filePath = "/Users/clymer/Desktop/pythonworkshop/2018_02_CooperWest/Text for processing/ScrabbleWordList.txt"
#filePath = "/Users/clymer/Desktop/pythonworkshop/2018_02_CooperWest/Text for processing/MiniWordList.txt"
# Open a new file object with the file path, and the "r" read mode
textFile = open(filePath, "r")
# Now, read the object into a string
text = textFile.read()
# Close the file once you're done
textFile.close()

# Testing some string methods:
#print( text )
#print( text.lower() )
#print(text.count("B"))
#print(text.replace("A", "Z"))
#print(text)


words = text.split("\n")

lettersUC = "ABCDEF"

foundWords = []
for word in words:
    # Start by assuming the word is good:
    goodWord = True
    # Check each letter in the word:
    for letter in word:
        # If it found a letter that wasn't in our set,
        # then the word is bad
        if not letter in lettersUC:
            goodWord = False
    if goodWord is True:
        # Append the good word to the list of found words
        foundWords.append(word)

#print(foundWords)

for i in range(21):
    print( random.choice(foundWords) )


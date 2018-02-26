import random

# Page size is 8.5 x 11
# Multiply by 72 points per inch to convert units
size(11*72, 8.5*72)

lettersUC = "AHONDG"
lettersLC = "nodais"
fontName = "Operator-Medium"
fontSize = 124

# Name parts of the page, to reuse them:
leftMargin = 1 * 72  # one inch times 72 points
bottomMargin = 1 * 72
textBoxWidth = 9 * 72
textBoxHeight = 6.5 * 72
textAreaSize = (leftMargin, bottomMargin, textBoxWidth, textBoxHeight)
textAreaHalfSize = (leftMargin, bottomMargin, textBoxWidth/2, textBoxHeight)
# It's okay to add line breaks within the parenthesis () after each comma
textAreaHalfSizeRight = (leftMargin+textBoxWidth/2, 
                         bottomMargin, 
                         textBoxWidth/2, 
                         textBoxHeight)


# Page 1:
# Large text showing of the full character set

font(fontName, fontSize)
lineHeight(fontSize * 1.2)
# Combine the strings by adding them,
# use the "\n" character for a new line break
textBox(lettersUC + "\n" + lettersLC, textAreaSize)
#rect(72, 72, 9*72, 6.5*72)

# Page 2:
# Spacing strings

newPage()
font(fontName, 25)

spacingText = ""
# Take each letter one at a time...
for letter in lettersUC:
    # ...and add it to the Spacing Text along with some control letters
    spacingText = spacingText + "HH" + letter + "HHOO" + letter + "OO\n"
textBox(spacingText, textAreaHalfSize)

spacingText = ""
# Take each letter one at a time...
for letter in lettersLC:
    # ...and add it to the Spacing Text along with some control letters
    spacingText = spacingText + "nn" + letter + "nnoo" + letter + "oo\n"
textBox(spacingText, textAreaHalfSizeRight)


# Page 3: Cap Text

filePath = "/Users/clymer/Desktop/pythonworkshop/2018_02_CooperWest/Text for processing/ScrabbleWordList.txt"
#filePath = "/Users/clymer/Desktop/pythonworkshop/2018_02_CooperWest/Text for processing/MiniWordList.txt"
# Open a new file object with the file path, and the "r" read mode
textFile = open(filePath, "r")
# Now, read the object into a string
text = textFile.read()
# Close the file once you're done
textFile.close()

words = text.split("\n")

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

storyText = ""
for i in range(21):
    #print( random.choice(foundWords) )
    storyText = storyText + random.choice(foundWords) + " "
print(storyText)

newPage()
font(fontName, 25)
textBox(storyText, textAreaHalfSize)

  

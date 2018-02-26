import random


# IDEAS TO CONTINUE:
# - Make several pages of text, with a few text sizes
#      == make the last few lines repeat with a range() loop
# - Capitalize the first letter of each LC word?
#      == ...only if the first letter is in the UC list!
# - Add the font name and the date and time, at least to the first page?
  

# Page size is 8.5 x 11
# Multiply by 72 points per inch to convert units
size(11*72, 8.5*72)

# The current character set, and the font to be proofed:
lettersUC = "ADHIOP"
lettersLC = "adeinops"
fontName = "Operator-Medium"
fontSize = 124

# Paths for the word list files
# (we'll use these names later in the script)
filePath = "/Users/clymer/Desktop/pythonworkshop/2018_02_CooperWest/Text for processing/ScrabbleWordList.txt"
# When you're testing you might want to use the smaller list, just uncomment this line when you want to do that:
#filePath = "/Users/clymer/Desktop/pythonworkshop/2018_02_CooperWest/Text for processing/MiniWordList.txt"

# Page setup:
# Name parts of the page, to reuse them:
leftMargin = 1 * 72  # one inch times 72 points
bottomMargin = 1 * 72
textBoxWidth = 9 * 72
textBoxHeight = 6.5 * 72
gutterWidth = 0.25 * 72 # a little bit of space between columns
textAreaSize = (leftMargin, bottomMargin, textBoxWidth, textBoxHeight)
textAreaHalfSize = (leftMargin, bottomMargin, textBoxWidth/2-gutterWidth, textBoxHeight)
# It's okay to add line breaks within the parenthesis () after each comma
textAreaHalfSizeRight = (leftMargin+textBoxWidth/2, 
                         bottomMargin, 
                         textBoxWidth/2-gutterWidth, 
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




# Page 3:
# Sample Text


# Open a new file object with the file path, and the "r" read mode
# The filePath was defined at the start of the document
textFile = open(filePath, "r")
# Now, read the object into a string
text = textFile.read()
# Close the file once you're done
textFile.close()

# Have the string split itself into a list, 
# every where a new line "\n" shows up in text
words = text.split("\n")

# Look at each word, and keep it only if all of its letters are in the characterset that we're proofing
foundWordsUC = [] # An empty list now, but it will fill up with the matching UC words
foundWordsLC = [] # and another list for the lowercase words
for word in words:
    # Start by assuming the word is good:
    goodWordUC = True
    goodWordLC = True
    # Check each letter in the word:
    for letter in word:
        # If it found a letter that wasn't in our set,
        # then the word is bad
        if not letter in lettersUC:
            goodWordUC = False
    # Now check the lowercase version of the word
    for letter in word.lower():
        if not letter in lettersLC:
            goodWordLC = False
    # At this point it's finished checking each letter in the word
    # If it was a good word:
    if goodWordUC is True:
        # Append the good word to the list of found words
        foundWordsUC.append(word)
    # And the same for the LC
    if goodWordLC is True:
        foundWordsLC.append(word.lower()) # keep the lowercase version of the word

# Turn the list of words into a text
# Adjust the range to choose how many words should be in the text
storyTextUC = ""
for i in range(200):
    storyTextUC = storyTextUC + random.choice(foundWordsUC) + " "
# Repeat the same thing for the LC, have it build some lowercase text
storyTextLC = ""
for i in range(200):
    storyTextLC = storyTextLC + random.choice(foundWordsLC) + " "

# Now, make a new page and draw it
newPage()
font(fontName, 12)
# UC on the left:
textBox(storyTextUC, textAreaHalfSize)
# LC on the right:
textBox(storyTextLC, textAreaHalfSizeRight)


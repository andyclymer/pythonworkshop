import random

size(200, 200)

for page in range(10):
    
    print page
    if page > 0:
        newPage()
        frameDuration(1/10)
    
    for x in range(0, 200, 20):
        for y in range(0, 200, 20):
            # Roll the dice:
            if random.random() > 0.5:
                fill(0.5, 0, 1)
                rect(x, y, page, 10)
            else:
                fill(1, 0, 0)
                #oval(x, y, 10, 10)
                letters = "ABDEFGHIJKLMNOPQRSTUVWXYZ"
                myLetter = random.choice(letters)
                fonts = installedFonts()
                theFont = random.choice(fonts)
                font(theFont, 14)
                text(myLetter	, (x, y))




newPage()

#saveImage("/Users/clymer/Desktop/Python Workshop/Class/animation.gif")


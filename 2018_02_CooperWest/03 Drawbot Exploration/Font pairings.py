import random


fonts = installedFonts()

headlineFont = random.choice(fonts)
textFont = random.choice(fonts)
print(headlineFont)
print(textFont)
size(200, 300)

font(headlineFont, 30)
text("Headline", (30, 250))

font(textFont, 10)
story = """Install a font with a given path and the postscript font name will be returned. The postscript font name can be used to set the font as the active font.

Fonts are installed only for the current process. Fonts will not be accesible outside the scope of drawBot.

All installed fonts will automatically be uninstalled when the script is done.
"""
textBox(story, (30, 30, 150, 200))

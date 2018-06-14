import random
font = CurrentFont()
# long way
# for glyph in font:
#     if glyph.name == 'Q':
#         print glyph

# better way
# print(font['Q'])
# a font can behave like a dictionary, but is not exactly one
# print(type(font))
# unordered list of glyph names
# print(font.keys())
# ordered list of glyph names
# print(font.glyphOrder)

glyph_name = 'Qgrave'

if glyph_name not in font:
    font.newGlyph(glyph_name)

glyph = font[glyph_name]
glyph.clear()
random_x = random.randint(-100, 100)
random_y = random.randint(-100, 100)
glyph.appendComponent('Q', offset=(random_x, random_y))

print(glyph.components)
print(len(glyph.components))

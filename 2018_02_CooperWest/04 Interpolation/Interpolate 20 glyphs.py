
font = CurrentFont()
minGlyph = font["a"]
maxGlyph = font["c"]
print("Compatibility report:")
print( minGlyph.isCompatible(maxGlyph) )

for i in range(21):
    print(i)
    factor = i / 20
    print(factor)
    percent = int(factor * 100)
    print(percent)
    glyphName = "interp" + str(percent)
    print(glyphName)
    interpGlyph = font.newGlyph(glyphName)
    print(interpGlyph)
    interpGlyph.interpolate(factor, minGlyph, maxGlyph)

    
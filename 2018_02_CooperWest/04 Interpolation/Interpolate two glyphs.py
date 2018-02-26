

# "Make this glyph the interpolation between minGlyph and maxGlyph by factor."

# minGlyph
# maxGlyph
# factor
font = CurrentFont()
minGlyph = font["a"]
maxGlyph = font["c"]
print("Compatibility report:")
print( minGlyph.isCompatible(maxGlyph) )

# Need a new glyph to draw the interpolation into
interpGlyph = font.newGlyph("b")
print(interpGlyph)
interpGlyph.interpolate(0.5, minGlyph, maxGlyph)

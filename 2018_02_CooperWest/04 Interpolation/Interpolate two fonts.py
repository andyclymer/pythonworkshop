from robofab.interface.all.dialogs import SelectFont

# Interpolate two fonts

font1 = SelectFont("Select the first font")
font2 = SelectFont("Now, Select the second font")
destinationFont = NewFont()

factor = 0.5

# Each glyph in the first font:
for glyphName in font1.glyphOrder:
    # If this glyph exists in the second font:
    if glyphName in font2:
        # Collect the glyph with the same name from both fonts
        glyph1 = font1[glyphName]
        glyph2 = font2[glyphName]
        # Get the glyph compatibility report
        report = glyph1.isCompatible(glyph2)
        # If the glyphs are compatible for interpolation:
        if report[0] == True:
            # Make a new glyph in the destination font
            newGlyph = destinationFont.newGlyph(glyphName)
            # Make the new glyph interpolate the other two glyphs, at the "factor" percentage
            newGlyph.interpolate(factor, glyph1, glyph2)
            
# Now that the interpolation is complete, sort the new destination font         
destinationFont.glyphOrder = font1.glyphOrder

print "Done interpolating!"

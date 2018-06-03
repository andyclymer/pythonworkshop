from robofab.interface.all.dialogs import SelectFont

# Test the interpolation compatibility for all glyphs in two fonts

font1 = SelectFont("Select the first font")
font2 = SelectFont("Now, Select the second font")

# Each glyph in the first font:
for glyphName in font1.glyphOrder:
    # If this glyph exists in the second font:
    if glyphName in font2:
        # Collect the glyph with the same name from both fonts
        glyph1 = font1[glyphName]
        glyph2 = font2[glyphName]
        # Get the glyph compatibility report
        report = glyph1.isCompatible(glyph2)
        # If something is incompatible, print the report
        if report[0] == False:
            print(glyphName, report)    
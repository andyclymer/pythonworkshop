from __future__ import print_function, division
# colorsys is a module that allows conversion of HSL values to RGB
import colorsys

f = CurrentFont()
# find out which unicode values are present in the UFO
# This is called a 'list comprehensions'
unicode_values = [g.unicode for g in f if g.unicode]

# What is the difference between max and min Unicode values?
# Make sure we have an even color distribution no matter if the
# UFO is big or small.
unicode_gamut = max(unicode_values) - min(unicode_values)
# If the difference of Unicode values is huge, we may end up with
# very slightly differently-marked glyphs. Better to keep the gamut small,
# for clear mark distinction
if unicode_gamut > 256:
    unicode_gamut = 256

# Hue/Saturation/Luminance values go from 0 to 1.
# fixed saturation:
saturation = 1
# fixed luminance:
luminance = 0.5
# The hue is flexible.
# The minimal step to cover all glyphs in the
# range of Unicode values is 1/unicode_gamut.
hue_step = 1 / unicode_gamut

# iterate through every glyph in the font
for g in f:
    # check if the glyph has a Unicode value
    if g.unicode:
        # calculate the hue value
        # % is the so–called "modulo" operator, which checks
        # a division for a remainder, e.g. 6 % 4 = 2
        # By using the modulo operator, we make sure that any
        # Unicode value relates to 256.
        hue = g.unicode % unicode_gamut * hue_step
        # Convert the HLS color to RGB
        h, l, s = colorsys.hls_to_rgb(
            hue, luminance, saturation)
        # mark the glyph (the final 1 is the added alpha value.)
        g.mark = (h, l, s, 1)

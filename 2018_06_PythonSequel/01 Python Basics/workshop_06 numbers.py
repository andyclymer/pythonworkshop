from __future__ import print_function, division

number = 10
statement = 'Andy is the best teacher '
# math with strings
print(statement * number)
print(statement + statement)
print(number * number)
print(number / 100)

# normal division.
# Attention: Python 2 will do 'floor' division by default (see below), unless
# division is imported from __future__ (see above).
print(3 / 4)

# 'floor' division (chops off everything behind the comma)
# The idea is that the result of an operation with two integers
# still results in an integer.
print(3 // 4)

# rounding
print(round(3 / 4))

# normal division even in Python 2
print(3 / 4.0)

# strings cannot be multiplied with numbers
print(str(number) * number)
print()

# get to a character by hexadecimal value (Unicode value)
print(0x006D)

# (silly) conversion of a character to a number, back to a character
print(chr(ord('m')))

# (even sillier) conversion of a character to a number,
# to a hex value, back to an integer, back to a character.
# print(chr(int(hex(ord('m'))), 16))
print(chr(int(hex(ord('m')), 16)))

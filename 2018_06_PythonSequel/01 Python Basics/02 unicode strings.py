# coding: utf-8
from __future__ import print_function

# A string can contain characters beyond ASCII.
# The utf-8 flag at the top of the file makes that possible.
# This illustrates the difference between a byte string and a Unicode string:
your_teachers = 'Aindriú O’Clymer & Frank Grießhammer 🌳'
your_teachers_unicode = u'Aindriú O’Clymer & Frank Grießhammer 🌳'

# Find out the length of a string with the len() function.
# notice the length difference!
print(your_teachers)
print(len(your_teachers))

print(your_teachers_unicode)
print(len(your_teachers_unicode))

for index, character in enumerate(your_teachers):
    print(index, character)

for index, character in enumerate(your_teachers_unicode):
    print(index, character)

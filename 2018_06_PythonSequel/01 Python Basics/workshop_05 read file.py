from __future__ import print_function

# open file
# (the text file is stored next to the script file.)
# The file we read is available here:
# https://github.com/adobe-type-tools/agl-aglfn/blob/master/aglfn.txt
text_file = open('aglfn.txt')
# read the data from the file into a string
raw_text = text_file.read()
# split the string by the line break
text_lines = raw_text.splitlines()

# concatenate all above lines into a single line:
# text_data = open('aglfn.txt').read().splitlines()

# print(type(text_file))
# print(type(raw_text))
# print(type(text_lines))

# print(text_lines[:10])
for line in text_lines:
    if line:
        # if the line does not start with a hash, print it
        if not line.strip().startswith('#'):
            # print the first four characters
            # (Unicode values in this list have only 4 digits)
            # print(line[0:4])

            # split the line by the semicolon to create a list
            # the line contains unicode value, glyph name, glyph description
            data_list = line.split(';')
            unicode_value, glyph_name, glyph_description = data_list
            # unicode_value, glyph_name = data_list[:2]
            if 'GREEK' in glyph_description:
                # print(unicode_value, glyph_name)
                # print(glyph_name, end=' ')
                print(unicode_value)
                # print()
            # if the word GREEK is in the glyph_description:
            #     print(glyph_name)

        # in any other case, do nothing (excluding the hash)
        else:
            pass

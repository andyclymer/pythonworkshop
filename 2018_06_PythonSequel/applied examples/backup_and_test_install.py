from __future__ import print_function
import time
import os
# more flourished date & time indication
# time_string = time.strftime('Week %U, %A %B %d, %H:%M')
# purely numerical

# find the current date and time and format it
# (formatting strings are here: https://docs.python.org/2/library/time.html)
time_string = time.strftime('%Y_%m_%d at %H-%M-%S')
# let's get to the font we are working on
font = CurrentFont()
# this is the full path to the UFO
ufo_path = font.path
# we split the path by the slash
# ufo_path_list = ufo_path.split('/')
# re-join the path with slash, minus the last item
# ufo_folder_path = '/'.join(ufo_path_list[:-1]) + '/'

# actually, this is easier:
# generate new font name for the otf file
otf_path = ufo_path[:-4] + ' ' + time_string + '.otf'
# otf_path = '/Users/fgriessh/Desktop/important_file.txt'

if os.path.exists(otf_path):
    print('This file already exists and will not be overwritten.')
else:
    font.generate(
        otf_path,
        'otf',
        # checkOutlines removes overlaps
        checkOutlines=True)

if not os.path.exists(otf_path):
    print('uh - oh. There was a problem')
else:
    print('done')

font.testInstall()

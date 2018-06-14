from __future__ import print_function
from vanilla import FloatingWindow, CheckBox, SquareButton
import time
import os

'''
This script is a small window in Robofont, which allows test-installing
the open font, as well as writing a dated backup OTF file adjacent
to the original UFO.

This script was written by/for students in the workshop
    Python -- The Sequel (with Andy Clymer and Frank Grießhammer)
    on June 13th, 2018, Type@Cooper, NYC
'''


class TestInstallBackup(object):

    def __init__(self):
        self.w = FloatingWindow(
            (120, 140),
            minSize=(100, 40),
            textured=True,
        )
        self.w.ti_checkbox = CheckBox(
            (10, 10, -10, 20),
            'Test Install',
            value=True
        )
        self.w.otf_checkbox = CheckBox(
            (10, 30, -10, 20),
            'OTF Backup',
            value=True
        )
        self.w.button = SquareButton(
            (10, 60, -10, -10),
            'GO',
            callback=self.button_callback
        )

        self.w.open()

    def build_otf(self, font):
        # this is the full path to the UFO
        ufo_path = font.path
        # the time string added to the file name
        time_string = time.strftime('%Y_%m_%d at %H-%M-%S')
        # the path to the final OTF
        otf_path = ufo_path[:-4] + ' ' + time_string + '.otf'

        # do not overwrite existing file
        if os.path.exists(otf_path):
            print('This file already exists and will not be overwritten.')
        else:
            # generate the OTF
            font.generate(
                otf_path,
                'otf',
                # checkOutlines removes overlaps
                checkOutlines=True,
            )
        # if the output path does not exist,
        # the font could not be generated.
        if not os.path.exists(otf_path):
            print('uh - oh. There was a problem')

        print(otf_path)

    def button_callback(self, sender):
        # Collect the state of the checkboxes
        test_install_state = self.w.ti_checkbox.get()
        build_otf_state = self.w.otf_checkbox.get()

        # Fetch the font and see if there even is one
        font = CurrentFont()
        if font:
            # let's see if the checkbox to build a UFO is checked.
            if build_otf_state:
                self.build_otf(font)
            # if the test install checkbox is checked
            if test_install_state:
                font.testInstall()
        else:
            print('No UFO open.')


TestInstallBackup()

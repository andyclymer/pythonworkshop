from __future__ import print_function
from vanilla import *
import time

'''
Based on Vanilla's button example, a button that prints the current time
when it is clicked. Also, the button has a favorite number.
'''


class TimeButton(object):

    def __init__(self):
        self.favorite_number = 123
        self.w = Window((120, 40))
        self.w.button = Button(
            (10, 10, -10, 20),
            "What time?",
            callback=self.buttonCallback)
        self.w.open()

    def buttonCallback(self, sender):
        # print "button hit!"
        print(time.strftime('%H:%M:%S'))


tb = TimeButton()
print(tb.favorite_number)

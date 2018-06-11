# Python libraries for working with fonts

Depending on the task at hand, there are several very useful Python libraries that you can "import" and use to either talk to your fonts or extend what you're capable of doing with Python. The libraries listed below come built-in with RoboFont and don't need any separate installation.

## If you want to write Python to...

### ...work with UFOs in RoboFont:

In RoboFont 1.8 you would make use of the **RoboFab** library of code, in RoboFont 3 you would use its relative **FontParts**. Think of FontParts as the new version of RoboFab, the concepts are the same but sometimes your code with be a little bit different.

RoboFab is documented on the RoboDocs website: http://robodocs.info/roboFabDocs/source/index.html
...and a great resource for the FontParts documentation can be found on RoboFont's website: http://robofont.com/documentation/building-tools/toolkit/fontparts/

The "Object Model" is shared between the two of them, for example, a "font" object is made up of "glyph" objects which are in turn made up of "contour" objects, but some of the function names have been updated in FontParts.

### ...edit the OTF or TTF font files directly (instead of editing UFOs)

Then you would import from the **FontTools** library of code. It can appear to be very complex to someone who’s new with Python, but it’s really very powerful to know that if you had to, you could make edits or read information out of OTFs after they’ve generated.

For instance you could have a Python script look through a folder full of OTF files and pick out the one that was missing a glyph. Or update font names without rebuilding the entire family. Lots of stuff like that. The FontTools library is alraedy installed in RoboFont and the API is documented on the RoboDocs website but the examples are a little bit limited... 
http://robodocs.info/fontToolsDocs/source/library/ttLib/init.html

### ...make windows and interfaces in RoboFont

You would use the **Vanilla** library of code. This is where things get really fun, once you’ve built a little “script” that works, why not make a nice little window interface for it! Vanilla is already included with RoboFont so you can already copy and paste directly from the Vanilla examples on the RoboDocs website:
http://robodocs.info/vanilla_index.html 

### ...draw PDFs, save images or make animations

You would use the **DrawBot** application, or if you install DrawBot as an extension in RoboFont you can make images or save PDFs from the same script that's interacting with a font.
http://www.drawbot.com/

### ...draw directly in the RoboFont interface

The outlines of your glyph will be drawn into a glyph window, but it's also possible to draw other shapes and text within the glyph view (imagine making an editing tool that displays measurements or highlights points in your drawing). RoboFont has a **Mojo** library with its own draiwng tools:
http://robofont.com/documentation/building-tools/toolkit/mojo/
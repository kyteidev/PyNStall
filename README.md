# PyNStall Copyright (c) 2022 LifeTecLover999. All rights reserved.
Distributed under the GNU General Public License v2, see LICENSE for details.

The best open-source Python app installer

# How to use
PyNStall is a highly customizable installer. It uses the Python TKinter GUI library.
To use, 
1. Download PyNSTall.py
2. Create new project in your IDE
3. replace main.py with PyNStall.py (If it was created by your IDE. If not, then drag PyNStall.py to your Python project directory)
4. Edit the following variables:
* versionsUrl - line 1 - this variable is used for providing version data to the version selector.
* cwd - line 16 - this is the directory in which PyNStall will install the app in
* versionstring - line 17 - this is optional. it shows PyNStall's current version
* MediaUrl - line 40 - this variable contains the url download link to your app. PyNStall has been tested with Mediafire but not sure if other file hosters work.
* filename - line 47 - NOTE: Only change the number. not sure how to explain, but heres an example: if your URL is set to mydomain.com/sample.exe/file then line 47 will automatically remove the "/file" part to identify your app version. Remove if you are planning to stick to one version.
* cwd - line 67 - path to the directory in which PyNStall will install the app in.
* window.title - line 100 - change it to your installer name
* title, subtitle, desc1 - line 114 to line 116 - change "PyNStall" to your installer name, the subtitle and the description respectively. You may change the font in variables on lines 114 to 120. Just modify the string next to font= (Remember to use fonts in the TKinter library!)

from line 158 to 172 you can edit the position of the widgets

and then from line 188 to line 203 change "PyNStall" to your installer name.

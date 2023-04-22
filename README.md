# Estimated one rep maximum calculator

Powerlifting and weight training with the barbell is a great way to display strength, but not everyone wants to test their one rep maximum all the time (or at all). This application allows the user to calculate their estimated one rep maximum (E1RM) using data from a recent set of any barbell exercise. Input your data into the application, press the calculate button, and voila! You can now estimate your maximal strength without having to do a maximal single, and can use your calculated e1rm to compare your strength over time without always needing to max out.

# How to use on your own machine (Ubuntu)

1. Download this folder (do not rename, as folder name is important for next steps)
2. Copy or move the py.desktop file to your desktop directory (if you make a copy: changes to py.desktop in the downloaded folder will not change the py.desktop file that is being executed when clicking on the icon)
3. Open folder in editor and open py.desktop
4. Update lines 3 & 5 (icon & exec) to the locations of the barbell-icon.png file (Icon) and the main.py file (Exec), by defualt they are set to the locations of these files on my machine
5. Open terminal window and execute the following commands with the location of main.py (first command) and location of py.desktop (second command):

    chmod u+x /home/<user>/<directory>/<python>.py
    
    then

    gio set /home/<user>/<directory>/<.desktop file> metadata:: trusted true
6. If clicking on the icon does not work, right click on the icon and click "allow launching"

# Contents

main.py: main python script using the pysimplegui library to create GUI

calculator.py: contains the e1rm calculation as a function

barbell-icon.png: png file for the desktop icon

py.desktop: desktop file that allows main.py to be ran via clicking on the barbell icon, created for ubuntu

README.md: this
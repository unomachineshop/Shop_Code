### Auto start a program after desktop loads (Graphical)  
1) With your prefered text editor you will need to edit the following file with super user privileges (sudo).
`sudo vim /etc/xdg/lxsession/LXDE-pi/autostart`  
  
2) Scroll down to the bottom of the file and add the following entry,  
`@python3 /home/pi/path/to/your/script.py`  
  
3) Understanding the command  
**@** - The @ sign is needed for all commands, it simply acts a delimeter allowing you to add multiple commands, delimited by the @ sign.   
  
**python3** - specifies what command line argument you would use to run your code. This is identical to what you would use on the command line to run/compile/invoke your code. 
Such as `javac, perl, python2, python3, etc`  
  
**/home/pi/path/to/your/script.py** - The last part is simply the absolute path to the entry point of your program. Ensure you have the absolute path, as relative pathing will not work.  

### Auto start a program after boot (Non Graphical)

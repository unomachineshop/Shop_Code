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
1) With your prefered text editor you will need to edit the following file with super user privileges (sudo).  
`sudo vim /etc/rc.local`  
  
2) Just before the `exit 0` command you will need to add the following entry,  
`python3 /home/pi/path/to/your/script.py &`  
  
3) Understanding the command  
**python3** - specifies what command line argument you would use to run your code. This is identical to what you would use on the command line to run/compile/invoke your code. 
Such as `javac, perl, python2, python3, etc` 
**/home/pi/path/to/your/script.py** - The last part is simply the absolute path to the entry point of your program. Ensure you have the absolute path, as relative pathing will not work.  
**&** - This specifies that the program should be run in the background, it's very important you add this because should something go wrong with your program you will be essentially locked out of your Pi. A simple reboot will not help, because upon each reboot, the program will crash, and cause your OS to hang.  
  
### Auto start program after specified time delay (Graphical or Non Graphical)
1) Run the following if your program does not require super user privileges,  
`crontab -e`  
If it does require super user privileges then run it with the following,  
`sudo crontab -e`  
  
2) Now go down to the bottom of the file and add the following,  
`@reboot sleep 90; python3 /home/pi/path/to/your/script.py`  
  
3) Understanding the command  
**@reboot** - Specifies to run this script on reboot.  
**sleep 90** - Specifies to wait 90 seconds before executing the script.  
**python3** - specifies what command line argument you would use to run your code. This is identical to what you would use on the command line to run/compile/invoke your code. 
Such as `javac, perl, python2, python3, etc`  
**/home/pi/path/to/your/script.py** - The last part is simply the absolute path to the entry point of your program. Ensure you have the absolute path, as relative pathing will not work.  

### Autostart and run program at specific time intervals indefinitely (Graphical or Non Graphical)  
1) Run the following if your program does not require super user privileges,  
`crontab -e`  
If it does require super user privileges then run it with the following,  
`sudo crontab -e`  
2) Scroll down to the bottom of the file and add the following,  
`*/2 * * * * python3 /home/pi/mshop/mshop/fileio/fileio.py`  
  
3) Understanding the command.  
*/2 * * * * - 
This is the crontab specifier, for this particular cron job, it will execute the specified script once every 2 minutes. Edit this as you see fit. Here is a basic outline of the allowed values,  
**Field    Description   Allowed Value**   
MIN      Minute field    0 to 59  
HOUR     Hour field      0 to 23  
DOM      Day of Month    1-31  
MON      Month field     1-12  
DOW      Day Of Week     0-6  
CMD      Command         Any command to be executed.  

  

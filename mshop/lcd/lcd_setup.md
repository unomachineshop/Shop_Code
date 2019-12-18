### Basic Setup for TFT Touchscreen
All credit for this guide goes to the following website tutorial.
https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/easy-install-2  
  
The actual script is saved in this github repository as well, in the very off chance it were to get removed from the adafruit website.  
  
You will need to run the following in order to download the script and run it,  
```
cd ~
get https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/adafruit-pitft.sh  
chmod +x adafruit-pitft.sh  
sudo ./adafruit-pitft.sh  
```
  
The script itself is very easy to follow, you will choose which type of screen you are currently using, the screen orientation, and whether you will be using command line (Non Graphical) or mirroring the HDMI output (Graphical).  
  
Should you need to remove the capabilities of the screen, you can re run the script, but decline all the options, which will return you back to a default state. Please note the installed software will still be there, it will just be disabled.

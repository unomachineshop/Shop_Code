### Stand Alone ###
#########################################################
# Name: create_datetime_file
# Desc: Creates a single file within specified path.
# This file's name is a simple date/time 
# string, ensuring all future file creations will have
# a unique name.
#########################################################
def create_datetime_file(path, data, ext=".txt"):
    from datetime import datetime

    file_name = datetime.now().strftime("%d-%m-%Y_%H:%M:%S") + ext
    try:
        with open(path, 'a') as f:
            f.write(data + "\n")
    except IOError as e:
        print(e)

### Stand Alone ###
#########################################################
# Name: create_datetime_entry
# Desc: Creates a single line data entry within the
# specified file. Useful for data logging time sensitive
# information.
#########################################################
def create_datetime_entry(path, data):
    from datetime import datetime

    dt = datetime.now().strftime("%d-%m-%Y_%H:%M:%S ")
    try:
        with open(path, 'a+') as f:
            f.write(dt + data + "\n")
    except IOError as e:
        print(e)



### Modify ###
#########################################################
# Name: config_reader_yaml
# Desc: A YAML configuration file reader. Given a simple
# config file convert it into a usable python dict.
# Usesful for ommitting senstive data from source 
# control.
#########################################################
def config_reader_yaml(path):
    import yaml
    with open(path) as config_file:
        data = yaml.load(config_file, Loader=yaml.FullLoader)
        
        #print(data)
        #print(data["username"])

### Modify ###
#########################################################
# Name: config_reader_yaml
# Desc: A YAML configuration file reader. Given a simple
# config file convert it into a usable python dict.
# Usesful for ommitting senstive data from source 
# control.
#########################################################
def config_reader_json(path):
    import json
    with open(path) as config_file:
        data = json.load(config_file)
        
        #print(data)
        #print(data["username"])

### Modify ###
#########################################################
# Name: rpi_gpio
# Desc: Specify which pins you would like to use in the 
# pins list below. Will iterate through and print out 
# all active pins.
# 
# You can use command 'pinout' in terminal
# to check pinouts.
# GPIO Pins: 3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,
# 26,27,28,29,31,32,33,35,36,37,38,40
#########################################################
def rpi_gpio():
    import RPi.GPIO as gpio
    from pin import Pin
    import time
    
    # Define board pin mapping
    gpio.setmode(gpio.BCM)

    # Define YOUR pins here
    # Pin(BCM Pin Number, Pin Name, Pullupdown up=True down=False)
    pins = [
            Pin(14, "Pin 14", True),
            Pin(15, "Pin 15", True),
            Pin(18, "Pin 18", True)
            ]

    # Control loop, define your own expression here
    while True:
        
        # Iterate through pins
        for pin in pins:

            # Update each pins current value
            pin.read_data()

            
            # If pin is active
            if pin.value == 0:
                print(pin.name + " is active!")
                time.sleep(.1)


rpi_gpio()



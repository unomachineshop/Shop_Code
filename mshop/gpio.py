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

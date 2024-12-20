import board
from adafruit_seesaw import seesaw, rotaryio, digitalio
from pythonosc import udp_client
from time import time, sleep

#Establsing I2C connection with rotary encoders:

i2c = board.I2C()

qt_enc1 = seesaw.Seesaw(i2c, addr=0x39)
qt_enc2 = seesaw.Seesaw(i2c, addr=0x37)
qt_enc3 = seesaw.Seesaw(i2c, addr=0x3A)
qt_enc4 = seesaw.Seesaw(i2c, addr=0x38)
qt_enc5 = seesaw.Seesaw(i2c, addr=0x36)

#Defining UDP client for OSC communication:

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

#Reading rotary encoder:
    
qt_enc1.pin_mode(24, qt_enc1.INPUT_PULLUP)
qt_enc2.pin_mode(24, qt_enc2.INPUT_PULLUP)
qt_enc3.pin_mode(24, qt_enc3.INPUT_PULLUP)
qt_enc4.pin_mode(24, qt_enc4.INPUT_PULLUP)
qt_enc5.pin_mode(24, qt_enc5.INPUT_PULLUP)

#Configure pin user to read encoder one button presses:

qt_enc1.pin_mode(24, qt_enc1.INPUT_PULLUP)
button = digitalio.DigitalIO(qt_enc1, 24)

#Define threshold for a long press:
press_threshold = 0.7

#Function activated when button pressed:

def buttonPressed():
    
    press_time = time()
    
    while not button.value:
        sleep(0.1)
        
    release_time = time()
    press_duration = release_time - press_time
    
    if press_duration >= press_threshold:
        client.send_message("/button",2)
        print("press")
    else:
        client.send_message("/button",1)
        print("click")

#Setting initial value for the rotary encoder:

encoder1 = rotaryio.IncrementalEncoder(qt_enc1)
last_position1 = "0"
encoder2 = rotaryio.IncrementalEncoder(qt_enc2)
last_position2 = "0"
encoder3 = rotaryio.IncrementalEncoder(qt_enc3)
last_position3 = "0"
encoder4 = rotaryio.IncrementalEncoder(qt_enc4)
last_position4 = "0"
encoder5 = rotaryio.IncrementalEncoder(qt_enc5)
last_position5 = "0"

#Tracking the button state:
button_held = False

while True:
    # negate the position to make clockwise rotation positive
    position1 = encoder1.position
    position2 = -encoder2.position
    position3 = -encoder3.position
    position4 = -encoder4.position
    position5 = encoder5.position

    if position1 != last_position1:
        if int(format(position1)) < int(format(last_position1)):
            print("encoder one increasing")
            client.send_message("/encoderOne", 1)
        else:
            print("encoder one decreasing")
            client.send_message("/encoderOne", -1)
        last_position1 = position1
        
    if position2 != last_position2:
        if int(format(position2)) > int(format(last_position2)):
            print("encoder two increasing")
            client.send_message("/encoderTwo", 1)
        else:
            print("encoder two decreasing")
            client.send_message("/encoderTwo", -1)
        last_position2 = position2
        
    if position3 != last_position3:
        if int(format(position3)) > int(format(last_position3)):
            print("encoder three increasing")
            client.send_message("/encoderThree", 1)
        else:
            print("encoder three decreasing")
            client.send_message("/encoderThree", -1)
        last_position3 = position3
        
    if position4 != last_position4:
        if int(format(position4)) > int(format(last_position4)):
            print("encoder four increasing")
            client.send_message("/encoderFour", 1)
        else:
            print("encoder four decreasing")
            client.send_message("/encoderFour", -1)
        last_position4 = position4
       
    if position5 != last_position5:
        if int(format(position5)) > int(format(last_position5)):
            print("encoder five increasing")
            client.send_message("/encoderFive", 1)
        else:
            print("encoder five decreasing")
            client.send_message("/encoderFive", -1)
        last_position5 = position5
        
    if not button.value and not button_held:
        button_pressed = True
        buttonPressed()
    elif button.value and button_held:
        button_pressed = False
        
    sleep(0.1)

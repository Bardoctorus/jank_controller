# Legend: https://github.com/bayangan1991/PYXInput
# This virtual xinput device is wicked


# TODO implement a pipeline:
#       - Data comes in
#       - cleaned up for controller
#       - is it new data ? to controller : send old data

# This will need it's own timing and error checking at every step before we can speed it up.

# TODO check if you need another emulation step for Trackmania.



import serial
import pyxinput
import time
import sys

MyVirtual = pyxinput.vController()
# This reads the serial port of the RP2040, as long as it's closed in MU
# turns
ser = serial.Serial(
                    'COM8',
                    115200,
                    timeout=0,
                    parity=serial.PARITY_EVEN,
                    rtscts = 1
                    )


while True:
    s = ser.read(100)

    #parse it, get ruid of the extra crap
    # give it to the game controller.


    if (sys.getsizeof(s) > 33):
        p = s.decode()
        print (p)

        # this errors out sometimes trying to convert the float
        #make it something like if (converts p  to float without an error) -> set the value else do nothing.
        MyVirtual.set_value('AxisLx', float(p))
        # BIGGER PROBLEM it doesn't seem to register as movement at all, but it has worked before so huh?
        time.sleep(0.5)
        
        







# This works, it is read as a standard XBOX 360 xInput STANDARD GAMEPAD
# imgur of the tester https://i.imgur.com/YaM29K0.png
# while True:
#     MyVirtual.set_value('BtnA', 1)
#     MyVirtual.set_value('AxisLx', -0.5)
#     time.sleep(0.5)
#     MyVirtual.set_value('BtnA', 0)
#     MyVirtual.set_value('AxisLx', 0.5)
#     time.sleep(0.5)


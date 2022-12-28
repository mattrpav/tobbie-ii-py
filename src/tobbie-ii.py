from microbit import *

def tobbieii_walk_forward():
    print('tobbieii_walk_forward() invoked')
    if pin8.read_digital():
        pin13.write_digital(1)
        pin14.write_digital(0)

def tobbieii_walk_backward():
    print('tobbieii_walk_backward() invoked')
    if pin8.read_digital():
        pin13.write_digital(0)
        pin14.write_digital(1)

def tobbieii_walk_stop():
    print('tobbieii_walk_stop() invoked')
    pin13.write_digital(0)
    pin14.write_digital(0)

def tobbieii_rotate_left():
    print('tobbieii_rotate_left() invoked')
    pin15.write_digital(1)
    pin16.write_digital(0)
   
def tobbieii_rotate_right():
    print('tobbieii_rotate_right() invoked')
    pin15.write_digital(0)
    pin16.write_digital(1)

def tobbieii_rotate_stop():
    print('tobbieii_rotate_stop() invoked')
    pin15.write_digital(0)
    pin16.write_digital(0)

def tobbieii_infared_enable():
    pin12.write_digital(1)

def tobbieii_infared_disable():
    pin12.write_digital(0)

def tobbieii_infared_right():
    return pin1.read_analog()
    
def tobbieii_infared_left():
    return pin2.read_analog()
    
while True:
    display.scroll('Hello, World!')
    display.show(Image.HEART)
    sleep(2000)
    tobbieii_rotate_right()
    sleep(2000)
    tobbieii_rotate_stop()
    sleep(2000)
    tobbieii_rotate_left()
    sleep(2000)
    tobbieii_rotate_stop()
    sleep(2000)
    tobbieii_walk_forward()
    sleep(2000)
    tobbieii_walk_stop()
    sleep(2000)
    tobbieii_walk_backward()
    sleep(2000)
    tobbieii_walk_stop()
    sleep(2000)


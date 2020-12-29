from microbit import *

def tobbieii_walk_forward():
    print('walk_forward() invoked')
    if pin8.read_digital():
        pin13.write_digital(1)
        pin14.write_digital(0)
        
def tobbieii_walk_backward():
    print('walk_backward() invoked')
    if pin8.read_digital():
        pin13.write_digital(0)
        pin14.write_digital(1)

def tobbieii_walk_stop():
    print('walk_stop() invoked')
    pin13.write_digital(0)
    pin14.write_digital(0)
    
def tobbieii_rotate_right():
    print('rotate_right() invoked')
    pin15.write_digital(0)
    pin16.write_digital(1)

def tobbieii_rotate_stop():
    print('rotate_stop() invoked')
    pin15.write_digital(0)
    pin16.write_digital(0)

while True:
    display.scroll('Hello, World!')
    display.show(Image.HEART)
    sleep(2000)
    rotate_right()
    sleep(2000)
    rotate_stop()
    sleep(2000)
    walk_forward()
    sleep(2000)
    walk_stop()
    sleep(2000)
    walk_backward()
    sleep(2000)
    walk_stop()

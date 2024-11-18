import pyfirmata
import time
import inspect

        
board=pyfirmata.Arduino('COM6')

it = pyfirmata.util.Iterator(board)
it.start()

pin9 = board.get_pin('d:9:s') # s para servo
angle = 0

while True:
    pin9.write(angle)
    time.sleep(1)
    angle += 10
    if angle >= 180:
        angle = 0
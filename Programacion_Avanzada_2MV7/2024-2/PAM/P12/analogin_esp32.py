import pyfirmata
import time
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

board = pyfirmata.Arduino('/dev/cu.usbserial-0001')

it = pyfirmata.util.Iterator(board)
it.start()

analog_value = 0

def handle_read(*data):
    global analog_value
    #print(data)
    analog_value = sum(data)/1023
    print(analog_value)

board.add_cmd_handler(0x02, handle_read)

while True:
    board.send_sysex(0x02, [12])
    if analog_value is not None:
        delay = analog_value
        board.send_sysex(0x01, [13, 1])
        time.sleep(delay)
        board.send_sysex(0x01, [13, 0])
        time.sleep(delay)
    else:
        time.sleep(0.1)


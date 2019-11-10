import pyfirmata
import time

# don't forget to change the serial port to suit
# port number of the arduino
board = pyfirmata.Arduino(r'/COM7 (Arduino/Genuino Uno)')

# start an iterator thread so
# serial buffer doesn't overflow
it = pyfirmata.util.Iterator(board)
it.start()

# set up pin D9 as Servo Output
pin9 = board.get_pin('d:9:s')

def move_servo(a):
    pin9.write(a)

degrees = [123,345,562,67,2,4657,7,234]
for deg in degrees:
    move_servo(deg)

print('end of program')

# board.digital[10].mode = pyfirmata.INPUT
#
# while True:
#     sw = board.digital[10].read()
#     if sw is True:
#         board.digital[13].write(1)
#     else:
#         board.digital[13].write(0)
#     time.sleep(0.1)

import serial                                           # import serial library
arduino = serial.Serial('/dev/cu.usbmodem1421', 9600)   # create serial object named arduino
while True:                                             # create loop

        command = str(input ("Servo position: "))       # query servo position
        arduino.write(command)                          # write position to serial port
        reachedPos = str(arduino.readline())            # read serial port for arduino echo
        print  reachedPos   

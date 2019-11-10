import os
credential_path = '/Users/jonathan/Desktop/HackPrinceton 2019-20aedb9bf596.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io

##############################
### TEXT TO SPEECH IS HERE ###
##############################
def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    import io
    client = speech.SpeechClient()

    # [START speech_python_migration_sync_request]
    # [START speech_python_migration_config]
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='en-US',
        model='default',
        audio_channel_count=2)
    # [END speech_python_migration_config]

    # [START speech_python_migration_sync_response]
    response = client.recognize(config, audio)
    print(response)
    # [END speech_python_migration_sync_request]
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.

    sentence = ''
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))
        sentence  += ' ' + result.alternatives[0].transcript
    # [END speech_python_migration_sync_response]

    return sentence.strip()
# [END speech_transcribe_sync]

sentence = transcribe_file('/Users/jonathan/Desktop/test.wav')

##############################
### TEXT TO DEGREES HERE ##### also put everything else in the same for loop
##############################

# X, Y
letter_coords = {
    'A' : [(0,0), (0,2), (1,2), (1,1), (0,1), (1,1), (1,0)],
    'B' : [(0,0), (0,1), (0,2), (1,2), (1,1), (0,1), (1,1), (1,0), (0,0)],
    'C' : [(1,0), (0,0), (0,1), (0,2), (1,2)],
    'D' : [(0,0), (0,1), (0,2), (1,2), (1,1), (1,0), (0,0)],
    'E' : [(1,0), (0,0), (0,1), (0.5,1), (0,1), (0,2), (1,2)],
    'F' : [(0,0), (0,1), (0.5, 1), (0,1), (0,2), (1,2)],
    'G' : [(1,2), (0,2), (0,1), (0,0), (1,0), (1,1), (0.5,1)],
    'H' : [(0,0), (0,2), (0,1), (1,1), (1,2), (1,0)],
    'I' : [(0,2), (1,2), (0.5,2), (0.5,0), (0,0), (0.5,0), (1,0)],
    'J' : [(0,2), (1,2), (0.5,2), (0.5,0), (0,0), (0,0.5)],
    'K' : [(0,2), (0,0), (0,1), (1,2), (0,1), (1,0)],
    'L' : [(0,2), (0,0), (1,0)],
    'M' : [(0,0), (0,2), (0.5,1), (1,2), (1,0)],
    'N' : [(0,0), (0,2), (1,0), (1,2)],
    'O' : [(0,0), (0,2), (1,2), (1,0), (0,0)],
    'P' : [(0,0), (0,2), (1,2), (1,1), (0,1)],
    'Q' : [(1,0), (1,2), (0,2), (0,1), (1,1)],
    'R' : [(0,0), (0,2), (1,2), (1,1), (0,1), (1,0)],
    'S' : [(1,2), (0,2), (0,1), (1,1), (1,0), (0,0)],
    'T' : [(0,2), (1,2), (0.5,2), (0.5,0)],
    'U' : [(0,2), (0,0), (1,0), (1,2)],
    'V' : [(0,2), (0.5,0), (1,2)],
    'W' : [(0,2), (0,0), (0.5,1), (1,0), (1,2)],
    'X' : [(0,2), (1,0), (0.5,1), (1,2), (0.5,1), (0,0)],
    'Y' : [(0,2), (0.5,1), (1,2), (0.5,1), (0.5,0)],
    'Z' : [(0,2), (1,2), (0,0), (1,0)]
}
# will be a list of all chars, and all chars will be the list of their cords,
# and their cords will be a pair of ints representing where it is
all_cords = []
off_set = 10
### get list of x,y cords for the letter here
def get_coords(sentence, pixel_width=10):
    # x start position of the current letter being executed
    for char_num, letter in enumerate(sentence.upper()):
        print(letter)
        ### get list of x,y cords for the letter here
        coords = letter_coords[letter]

        # off_set_coords = []

        for x, y in coords:
            x = x * pixel_width + char_num * pixel_width * 2
            y = y * pixel_width
            # off_set_coords.append([x,y])
            all_cords.append([x,y])

            print([x,y])
        # all_cords.append(off_set_coords)


get_coords(sentence, 10)

print(all_cords)


### Kasia code here ###
import math
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


angleList = []
# letters = [(0,0),(0,20),(10,20),(10,10),(0,10),(10,10),(10,0),(15,0),(15,20),(25,20),(25,10),(15,10),(25,10),(25,0)]
letters = all_cords
numFrames = len(letters)

fig = plt.figure()
ax = plt.axes(xlim=(-10, 170), ylim=(-100, 50))
ax.set_title('Drawing arm')
ax.set_aspect('equal', 'box')
line, = ax.plot([], [], lw=3)

RADIANS = 0
DEGREES = 1

l1 = 100 #Length of link 1
l2 = 100 #length of link 2


def init():
    line.set_data([], [])
    return line,

def animate2(i):
    #x = endpointList[i][0]
    #y = endpointList[i][1]

    endpointList = letters

    x = endpointList[i][0]
    y = endpointList[i][1]

    [th1, th2, x_j, y_j] = invkin2(x, y, DEGREES)

    angleList.append((th1, th2))

    x_val = [n[0] for n in endpointList[:i+1]]
    y_val = [n[1] for n in endpointList[:i+1]]

    plt.plot(x_val, y_val,'m', zorder = 1)

    plotDot()

    xd = [0, x_j,x ]
    yd = [0, y_j,y ]

    line.set_data(xd, yd)
    return line,



#IK for just the 2 links
def invkin2(x, y, angleMode=DEGREES):
    """"
    Returns the angles of the first two links
    in the robotic arm as a list.
    returns -> (th1, th2)
    input:
    x - The x coordinate of the effector
    y - The y coordinate of the effector
    angleMode - tells the function to give the angle in
                degrees/radians. Default is degrees
    output:
    th1 - angle of the first link w.r.t ground
    th2 - angle of the second link w.r.t the first
    """

    #stuff for calculating th2
    r_2 = x**2 + y**2
    l_sq = l1**2 + l2**2
    term2 = (r_2 - l_sq)/(2*l1*l2)
    term1 = ((1 - term2**2)**0.5)*-1
    #calculate th2
    th2 = math.atan2(term1, term2)
    #optional line. Comment this one out if you
    #notice any problems
    th2 = -1*th2

    #Stuff for calculating th2
    k1 = l1 + l2*math.cos(th2)
    k2 = l2*math.sin(th2)
    r  = (k1**2 + k2**2)**0.5
    gamma = math.atan2(k2,k1)
    #calculate th1
    th1 = math.atan2(y,x) - gamma

    x_j = l1 * math.cos(th1)
    y_j = l1 * math.sin(th1)

    if(angleMode == RADIANS):
        return th1, th2, x_j, y_j
    else:
        return math.degrees(th1), math.degrees(th2), x_j, y_j


def plotDot():
    xdot = []
    ydot = []

   # rangeVal = int(numFrames/7)*75

    for n in range (10):
        xdot.append(n*15 -2.5)
        ydot.append(0)

    plt.scatter(xdot, ydot, c='w', s=45, zorder = 2)


anim = FuncAnimation(fig, animate2, init_func=init,
                     frames =numFrames, interval=100, blit=True)
anim.save('arm.html', writer='imagemagick')
print(angleList)
#######################

#################################
### Start of the arduino code ###
#################################
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

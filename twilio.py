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
### TEXT TO DEGREES HERE #####
##############################
# x start position of the current letter being executed
x_position = 0
for letter in sentence:
    # we onlt want to print out characters and skip the rest
    if letter is ' ':
        continue

        ### get list of x,y cords for the letter here
        coords_list = get_coords(letter)

        ### get set of degrees here (all movements for the arm)
        degrees_list = get_degrees(coords_list)

        ### do simmulation here or in the get degrees function
        

        ### move arduino arm
        move_arm(degrees_list)

### get list of x,y cords for the letter here
def get_coords(letter):
    pass


### get set of degrees here (all movements for the arm)
def get_degrees(coords_list):
    pass

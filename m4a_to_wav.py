import os,sys
folder = '/Users/jonathan/Desktop/audio'
for filename in os.listdir(folder):
   infilename = os.path.join(folder,filename)
if not os.path.isfile(infilename): continue
   oldbase = os.path.splitext(filename)
   newname = infilename.replace('.tmp', '.m4a')
   output = os.rename(infilename, newname)
# Convert m4a extension files to wav extension files
import os
import argparse
from pydub import AudioSegment
formats_to_convert = ['.m4a']
for (dirpath, dirnames, filenames) in os.walk(folder):
    for filename in filenames:
        if filename.endswith(tuple(formats_to_convert)):
            filepath = dirpath + '/' + filename
            (path, file_extension) = os.path.splitext(filepath)
            file_extension_final = file_extension.replace('.', '')
            try:
                track = AudioSegment.from_file(filepath, file_extension_final)
                wav_filename = filename.replace(file_extension_final, 'wav')
                wav_path = dirpath + '/' + wav_filename
                print('CONVERTING: ' + str(filepath))
                file_handle = track.export(wav_path, format='wav')
                os.remove(filepath)
            except:
                print("ERROR CONVERTING " + str(filepath))

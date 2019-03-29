from subprocess import Popen, PIPE
import requests
import base64
import os
from pydub import AudioSegment

def getFullAudio(audioURL, videoID):
    print('Getting complete audio file')
    r = requests.get(audioURL, stream=True)

    mainFile = b''
    for chunk in r.iter_content(chunk_size=4096):

        if encoded:
            outChunk = base64.b64encode(chunk)
        else:
            outChunk = chunk
        mainFile += outChunk

        try:
            os.makedirs('./data/' + videoID)
        except:
            pass

    f = open('./data/' + videoID + '/audio' + '.mp3', 'wb+')
    f.write(mainFile)
    f.close()

def getChunkedData(audioURL, videoID):
    print('Getting chunked audio data')
    r = requests.get(audioURL, stream=True)

    unitFileLength = 0

    i = 0
    fullFile = b''
    for chunk in r.iter_content(chunk_size=100*1024):

        if encoded:
            outChunk = base64.b64encode(chunk)
        else:
            outChunk = chunk
        
        try:
            os.makedirs('./data/' + videoID)
        except:
            pass
        
        fullFile += outChunk

        f = open('./data/' + videoID + '/chunk' + str(i) + '.mp3', 'wb+')
        f.write(fullFile)
        f.close()

        audioFile = AudioSegment.from_file('./data/' + videoID + '/chunk' + str(i) + '.mp3')

        if i == 0:
            unitFileLength = audioFile.duration_seconds

        audioFile = audioFile[-(unitFileLength * 1000):]
        audioFile.export('./data/' + videoID + '/chunk' + str(i) + '.mp3', format='mp3', bitrate='128k')

        i += 1
        print(i)

# change this to False if you want the decoded \x00-like format
encoded = False

videoID = 'ZAfAud_M_mg'
process = Popen(['youtube-dl', '--get-url', '-f', '140', 'https://www.youtube.com/watch?v=' + videoID], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
payloadURL = stdout.decode("utf-8") 
print(payloadURL)

getChunkedData(payloadURL, videoID)
#getFullAudio(payloadURL, videoID)
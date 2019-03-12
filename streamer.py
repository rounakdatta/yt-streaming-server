from subprocess import Popen, PIPE
import requests
import base64
import os

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

    i = 0
    for chunk in r.iter_content(chunk_size=15*1024):

        if encoded:
            outChunk = base64.b64encode(chunk)
        else:
            outChunk = chunk
        
        try:
            os.makedirs('./data/' + videoID)
        except:
            pass

        f = open('./data/' + videoID + '/chunk' + str(i) + '.mp3', 'wb+')
        f.write(outChunk)
        f.close()

        i += 1
        print(i)

# change this to False if you want the decoded \x00-like format
encoded = False

videoID = '8dsctieMibU'
process = Popen(['youtube-dl', '--get-url', '-f', '140', 'https://www.youtube.com/watch?v=' + videoID], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
payloadURL = stdout.decode("utf-8") 
print(payloadURL)

getChunkedData(payloadURL, videoID)
getFullAudio(payloadURL, videoID)
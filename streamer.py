from subprocess import Popen, PIPE
import requests
import base64

def getChunkedData(audioURL):

    r = requests.get(audioURL, stream=True)
    for chunk in r.iter_content(chunk_size=1024):

        if encoded:
            print(base64.b64encode(chunk))
        else:
            print(chunk)

        print()

# change this to False if you want the decoded \x00-like format
encoded = True

videoID = '8dsctieMibU'
process = Popen(['youtube-dl', '--get-url', '-f', '140', 'https://www.youtube.com/watch?v=' + videoID], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
payloadURL = stdout.decode("utf-8") 
print(payloadURL)

getChunkedData(payloadURL)
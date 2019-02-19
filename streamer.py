import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from subprocess import Popen, PIPE

videoID = '8dsctieMibU'
process = Popen(['youtube-dl', '--get-url', '-f', '140', 'https://www.youtube.com/watch?v=' + videoID], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
payloadURL = stdout.decode("utf-8") 
print(payloadURL)

http = urllib3.PoolManager()
r = http.request('GET', payloadURL, preload_content=False)

for chunk in r.stream(32):
    print(chunk)
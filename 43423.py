import requests

url = 'https://ayushcv.github.io'
file = {"myFile":open('/home/pi/Resources12/database','a')}
#Upload File
response = requests.post(url, files=file)
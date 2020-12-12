import json
import requests

filedirectory = '/home/pi/Resources12/database'
filename = 'database'
folderid = '1VbcH3MZYEj6WNeryD2b282J3I2oQehSm'
access_token = '368174336898-oaaah3llb1u44eulqe7cco9jg34ta2an.apps.googleusercontent.com'

metadata = {
    "name": filename,
    "parents": [folderid]
}
files = {
    'data': ('metadata', json.dumps(metadata), 'application/json'),
    'file': open(filedirectory, "rb").read()  # or  open(filedirectory, "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers={"Authorization": "Bearer " + access_token},
    files=files
)
print(r.text)
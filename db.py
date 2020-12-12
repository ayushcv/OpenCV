from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = '/home/pi/Downloads/client_secret_368174336898-oaaah3llb1u44eulqe7cco9jg34ta2an.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1VbcH3MZYEj6WNeryD2b282J3I2oQehSm'
file_names= ['database.txt']
mime_types= ['text/plain']

for file_name, mime_types in zip(file_names, mime_types):
    file_metadata={
        'name' : file_name,
        'parents' : [folder_id]
    }

    media = MediaFileUpload('/home/pi/Resources12/{0}'.format(file_name), mimetype=mime_types)

    service.files().create(
        body= file_metadata,
        media_body=media,
        fields='id'
    ).execute()

'''
For now:
    Received attachment and saves it to disc as a PDF with file name
Later:
    Send attachment to a Flask server
'''

import requests
import os
from dotenv import load_dotenv
load_dotenv()

ATTACHMENT_URL = os.getenv('ATTACHMENT_URL')
USERNAME = os.getenv('USERNAME')
AUTH_KEY = os.getenv('AUTH_KEY')

r = requests.get(ATTACHMENT_URL)
file_name = r.headers['Content-Disposition'].split('"')[1]
content = r.content

with open(file_name, 'wb') as f:
    f.write(content)

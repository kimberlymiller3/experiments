from curses import A_ALTCHARSET
from flask import Flask, render_template, request, redirect, url_for
import requests



app = Flask(__name__)

ATTACHMENT_URL = "https://downloads.regulations.gov/EPA-HQ-OW-2021-0602-0130/attachment_1.pdf"

def attachment_url():
    r = requests.get(ATTACHMENT_URL)
    file_name = r.headers['Content-Disposition'].split('"')[1]
    content = r.content
    return content, file_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    render_template('index.html')
    r = requests.get(ATTACHMENT_URL)
    file_name = r.headers['Content-Disposition'].split('"')[1]
    content = r.content
    if file_name != '':
        with open(file_name, 'wb') as f:
            f.write(content)
    return redirect(url_for('index'))

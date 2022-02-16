# experiments

### URL
https://downloads.regulations.gov/EPA-HQ-OW-2021-0602-0130/attachment_1.pdf

### Create and activate Virtual Environment
- python3 -m venv .venv
- source .venv/bin/activate

### Install dependices
- pip install requests
- pip install python-dotenv

### Create an .env file and add
- ATTACHMENT\_URL = the_attachemnt_url
- USERNAME = username_for_regulations_key
- AUTH\_KEY = your_regulations_key

### To run flask server
- pip install flask
- export FLASK_APP=flask_server.py
    - Change the .py file to whatever flask app you want to run
- export FLASK_ENV=development
- flask run

###this is our python initialization file. Its the first thing that gets read
##from here, it will call on Flask to read in the rest of the app we have

from flask import Flask

app = Flask(__name__)
app.config.from_object('config') ##enables Flask to read and use oour 'config.py file'

from app import views
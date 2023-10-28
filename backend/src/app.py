from flask import *
import db


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if (not (session.get('loginAttempted'))):
        session['loggedIn'] = False
        session['username'] = ""
        session['email'] = ""
    
    session['loginAttempted'] = True

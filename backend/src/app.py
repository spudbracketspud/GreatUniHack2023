from flask import *
import db


app = Flask(__name__)
session['loggedIn'] = False
session['username'] = ""
session['email'] = ""

@app.route("/", methods=['GET', 'POST'])
def home():
    if (not (session.get('loggedIn'))):
        return render_template('homePageNotLoggedIn.html')
    #Database Authentication for user
    session['loginAttempted'] = True

from flask import *
import db


app = Flask(__name__)
session['loggedIn'] = False
session['username'] = ""
session['email'] = ""

#Home Pages
@app.route("/", methods=['GET', 'POST'])
def home():
    if (not (session.get('loggedIn'))):
        return render_template('homePageNotLoggedIn.html')
    #Database Authentication for user
    return render_template('homePageLoggedIn.html')
    session['loginAttempted'] = True


#Log In / Registration
@app.route("/login", methods=['GET', 'POST'])
def login():
    if (session.get('loggedIn')):
        return redirect(url_for('home'))
    #Database Authentication for user
    session['loginAttempted'] = True

@app.route("/login", methods=['GET', 'POST'])
def login():
    if (session.get('loggedIn')):
        return redirect(url_for('home'))
    #Database Authentication for user
    session['loginAttempted'] = True

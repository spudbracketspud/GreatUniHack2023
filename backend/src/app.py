from flask import *
import db


app = Flask(__name__)


#Home Pages
@app.route("/", methods=['GET', 'POST'])
def home():
    #Database Authentication for user
    return render_template('homePageLoggedIn.html')

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('homePageLoggedIn.html')
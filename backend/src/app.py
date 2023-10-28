from flask import *
import db
import imageProcessing

app = Flask(__name__)

#Home Pages
@app.route("/", methods=['GET', 'POST'])
def home():
    #Database Authentication for user
    return render_template('homePage.html')

@app.route("/amazon", methods=['GET', 'POST'])
def Amazon():
    return render_template('amazonHome.html')

@app.route("/ankoro", methods=['GET', 'POST'])
def Amazon():
    return render_template('ankoro.html')

if __name__ == "__main__":
    #imageProcessing.processImage('greenCubeTest.jpeg')  -> returns a float of colour of green percentage
    app.run(debug=True)
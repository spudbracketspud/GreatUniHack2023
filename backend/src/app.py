from flask import *
import db
import imageProcessing

app = Flask(__name__)
def getCaptures(location):
    pass
    #create json of all the map tile values

#Home Pages
@app.route("/", methods=['GET', 'POST'])
def home():
    #Database Authentication for user
    return render_template('homePage.html')

@app.route("/amazon", methods=['GET'])
def Amazon():

    return 

@app.route("/ankoro", methods=['GET', 'POST'])
def Amazon():
    return render_template('ankoro.html')

if __name__ == "__main__":
    #imageProcessing.processImage('greenCubeTest.jpeg')  -> returns a float of colour of green percentage
    app.run(debug=True)
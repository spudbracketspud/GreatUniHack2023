from flask import *
import db
import imageProcessing

app = Flask(__name__)

#Home Pages
# @app.route("/", methods=['GET', 'POST'])
# def home():
#     #Database Authentication for user
#     return render_template('homePageLoggedIn.html')

# @app.route("/", methods=['GET', 'POST'])
# def home():
#     return render_template('homePageLoggedIn.html')


if __name__ == "__main__":
    #imageProcessing.processImage('greenCubeTest.jpeg')  -> returns a float of colour of green percentage
    app.run(debug=True)
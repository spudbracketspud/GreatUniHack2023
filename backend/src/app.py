from flask import *
#import db
import imageProcessing
import os

app = Flask(__name__)



def getCaptures(location):
    foliageList = []
    if location == "Amazon":
        prefix = 'a'
        
    filePath = "captures/"+prefix #capture/a or capture/i
    i = 1
    while (os.path.exists(filePath+str(i)+".jpeg")): 
        
        foliageList.append(imageProcessing.process(filePath+str(i)+".jpeg"))
        i += 1

    return foliageList


#Home Pages
@app.route("/", methods=['GET', 'POST'])
def home():
    #Database Authentication for user
    return render_template('homePage.html')

# @app.route("/amazon", methods=['GET'])
# def Amazon():

    # return 

@app.route("/ankoro", methods=['GET', 'POST'])
def Amazon():
    return render_template('ankoro.html')

if __name__ == "__main__":
    print(getCaptures("Amazon"))
    app.run(debug=True)
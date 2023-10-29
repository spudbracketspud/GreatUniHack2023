from flask import *
#import db
import imageProcessing
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
# @app.route("/", methods=['GET', 'POST'])
# def home():
#     #Database Authentication for user
#     return render_template('homePage.html')

# @app.route("/amazon", methods=['GET'])
# def Amazon():

#     return 

# @app.route("/ankoro", methods=['GET', 'POST'])
# def Amazon():
#     return render_template('ankoro.html')

if __name__ == "__main__":
    foliagePercnt = getCaptures("Amazon")
    print(foliagePercnt)
    averageFoliage = sum(foliagePercnt) / len(foliagePercnt)
    #assuming width is 2
    width = 3
    tempRow = []
    foliageArray = [foliagePercnt[i:i+width] for i in range(0, len(foliagePercnt), width)]
    x = []
    y = []
    for i in range (int(len(foliagePercnt) / width)):
        for j in range(width):
            x.append(j)
            y.append(i)
        

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, foliageArray, c='b', marker='o')
    ax.set_xlabel('Latatude')
    ax.set_ylabel('Longditude')
    ax.set_zlabel('Green Percentage')
    ax.set_title('3D Scatter Plot Example')
    plt.show()
    app.run(debug=False)
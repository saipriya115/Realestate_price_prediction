#so we will import the util file here
import util
from flask import Flask, request, jsonify
#flask module will allow us to write a python service which can serve http requests
app = Flask(__name__)


#first routine would be to return the locations in bangolore city and we have the locations
#in coloumn.json file
#in my ui application i want to have a dropdown where i want to show all the locations
#so for that i will write the routine which will show the locations
@app.route('/get_location_names', methods=['GET'])
#for locations i am going to create a new file called util and util will contain all the
#core routines whereas server will do the routing of requests and response s

def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
    #so here i am returning a response which is containing all the locations
@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    #now whenever we make a request to this particular route then we get request.form which
    #contains the four inputs below
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
#now it will run the application on specific port
import pickle
import json
import numpy as np
#i created 3 global variable s
__locations = None
__data_columns = None
__model = None
#now i need to write a function which returns price given bhk,location,sqft_area,bathroom
#etc
#we will not use np.where because it is a python list(__data_columns) np.where is used
#for numpy array whatever location we are getting it need to be converted into lower
#case because in coloumn.jsom we have columns in lower case
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)
#here we are making that specific index column as 1 and remaining as 0



def get_location_names():
    return __locations
def load_saved_artifacts():
#this method is used to load the artifacts and i am going to store these artifacts in
#the global variable
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']#whatever object is loaded will be
        #converted into dictionary on which we can call datacolumns key and that
        #will return my datacolumns

        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
#so here get_location_names should read column.json and and it should return the list of all
#locations
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
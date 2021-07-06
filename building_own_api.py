from flask import Flask, jsonify, request
from api_work.flights_data import flights
from api_work.utils import search_flight, get_index

#jsonify, converts input into a jon object. JSON is key value pairs. 
#request is the request library to make requests to the API.
#get functionss from utils, get data from flights

app = Flask(__name__)
#initialising

# GETTING INFORMATION

@app.route('/')
def hello():
    return {'hello': 'Universe'}
#only needs a slash, returns an object with key hello and value universe. 
# flask -- help
#cd api_work - to change directory
#export FLASK_APP= building_own.api
#flask run 
#copy and paste address. The route is simply with a slash. 

@app.route('/flights')
def get_flights():
    return jsonify(flights)

#passing in flights, passing it to jsonify which gives it back as a JSON object. 
#This shows all the info for the flight data. 

# http://127.0.0.1:5000/flights


@app.route('/flights/<int:id>')
def get_flight_by_id(id):
    flight = search_flight(id, flights)
    return jsonify(flight)

#gets a very specific flight, flight by ID. int:id, this is the end point.
#id is an int, <> this is the input we need to give it to fetch that data and return
#using search flight function - store it as a variable flight. then returning that flight. 
#enter that after slash, enteer for results. no search box function. 

# http://127.0.0.1:5000/flights/555


# ADDING NEW FLIGHTS

@app.route('/flights', methods=['POST'])
def add_flight():
    flight = request.get_json()
    flights.append(flight)
    return flight

#post - creates a new resource. 
#adds a new flight. similar to one above in flight. we specify method as post. method
#by default, the method is GET before. 
#same endpoint, but specify a method of post. how do we call this and give it that data.  
#request.get_json() another method of getting that data. whataver data you're getting
#just creating the function currently. not passing through any actual data.
#we're the ones defining the endpoints, since we're the creators - this endpoint specifies flights


# UPDATING A FLIGHT


@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    flight_to_update = request.get_json()
    index = get_index(id, flights)
    flights[index] = flight_to_update
    return jsonify(flights[index])

#Updating is a PUT method. Getting flight by ID and then specifically changing it. 
#this is the function we have to execute, passing through the flight ID.
#the id already exists, id in brackets. get index from utils. 
#got the index, and the data we're updating it to. flights index updated to new data. return that.

# DELETING A FLIGHT


@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    index = get_index(id, flights)
    deleted = flights.pop(index)
    return jsonify(deleted), 200

#pass all through the end point. once we have the index, can just pop and return the remaining flights. 

if __name__ == '__main__':
    app.run(debug=True)





def search_flight(fid, flights):
    return [element for element in flights if element['flight_id'] == fid]


def get_index(fid, flights):
    for i, flight in enumerate(flights):
        if flight['flight_id'] == fid:
            return i
    return -1

#a number of helper functions that we're using. 
#search flight - gets flight id and flight data - list flights.  
#takes in flight id and data, returns object for that flight. list comprehension. returns
#shorter way to write a for loop. if element == fid, it will return that element. else
#So, the element is just like i or n in a for loop, simply an object and you're iterating
#through a list to find a match. in this case, the match is the flight id, the location is flights data.
# RANDOM THOUGHT - try changing it to something more representative. i.e. if id == fid. ?

#get index - i is the index, flight is the object. This is a cool thing python can do in essentially
#returning key value pairs again, letting you search for a specific thing.
#returns the index of that flight object. otherwise returns a -1, which
#which does not exist. 
#2 variables needed, first one always index and the second is the object. flight is flight object. flight
#goes through a list and returns something. Think a lot about how JSON data is in key value pairs, so that kind of
#thinking is how we would analyse the data.


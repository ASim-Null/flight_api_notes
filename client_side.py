import requests
import json

#POST REQUEST

new_flight = {
      "from_city": "Stockholm",
      "to_city": "Oslo",
      "days": [1, 7],
      "captain": {'name': 'Ole',
                  'surname': 'Johansson'},
      "duration_min": 30,
      "capacity": 50,
      "booked": 20,
      "available":  30,
      "flight_id": 777
 }

headers = {'content-type': 'application/json'}
result = requests.post(
    'http://127.0.0.1:5000/flights', headers=headers, data=json.dumps(new_flight)
)
print(result)

# a new flight dictionary contains the information for a new flights
#all the same information as the otherr key pairs. 
#call the requests.post() - pass in a few arguments, first is the endpoint, the address. 
#pass in a few headers and then pass the data that you've just created. 
#headers is a key value pair object, content type.  .dumps - serialise the object into JSON format. 
#then appends it to the flights list. We need to give it data, end point, headers and data. 
#200 is all ok. refresh endpoint. 



# PUT REQUEST

updated_flight = {
     "new content": "test",
     "flight_id": 555
}

fid = 555

headers = {'content-type': 'application/json'}
result = requests.put(
    'http://127.0.0.1:5000/flights/{}'.format(fid), headers=headers, data=json.dumps(updated_flight)
)
print(result)

#have to give it an id to update in the original file. giving it data, as you need to give it new data. The new
#content is very short, just test and flight id. same header, but the {} is V IMPORTANT.  
#CURLY BRACKETS are for input to the endpoint, leave it as a blank. Use .format and give it the input - in this case (fid) - 555.
#every time, you'll have to update the fid. these are reusable, once the web app has been updated. 
#run the clientside file to update and refresh. 



# DELETE REQUEST

fid = 555

headers = {'content-type': 'application/json'}
result = requests.delete(
    'http://127.0.0.1:5000/flights/{}'.format(fid), headers=headers
)

print(result)

#.delete is the request. endpoint is the placeholder for the id. delete so it does not need data parameters. 
# only when the method is delete. (look at main function)

#where we have the requests, where we put delete and post. 
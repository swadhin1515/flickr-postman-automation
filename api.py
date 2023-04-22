import requests
import json

# Define the API endpoint and parameters
url = "https://api.flickr.com/services/rest/"

photo_params = {'method': 'flickr.photos.getInfo',
    "api_key": "dfaae157024e53496e5e077232f2d3aa",
    "photo_id": "52813424160",
    "format": "json",
    'nojsoncallback': 1,
}
user_params = {
    'method': 'flickr.people.getInfo',
    "api_key": "dfaae157024e53496e5e077232f2d3aa", 
    "user_id": "198154279@N07", 
    "format": "json",
    'nojsoncallback': 1,
}




# Make the API request
photo_response = requests.get(url, params=photo_params)
user_response = requests.get(url, params=user_params)

# Check if the response was successful (status code 200)
if photo_response.status_code == 200:
 # Decode the JSON response and extract specific information
    photo_data = json.loads(photo_response.content)
      # prints an array of photo objects
else:
    print("Error: API request unsuccessful.")

#user responce 
user_response = requests.get(url, params=user_params)

if user_response.status_code == 200:
    user_data = json.loads(user_response.content)
   
else:
    print(f"Error: {user_response.status_code} - {user_response.reason}")


# Extract data points from the responses
photo_title = photo_data["photo"]["title"]["_content"]
photo_tags = photo_data["photo"]["tags"]["tag"]
user_realname = user_data["person"]["realname"]["_content"]
user_location = user_data["person"]["location"]["_content"]


# Print the extracted data
print("Photo Title: " + photo_title)
print("Photo Tags: " + str(photo_tags))
print("User Real Name: " + user_realname)
print("User Location: " + user_location)

import requests

# Define the API endpoint URL
api_url = "http://localhost/attendance/savestudent.php"

# Define headers if needed (e.g., for authentication)
headers = {
    "Authorization": "Bearer your_access_token",
    "Content-Type": "application/json"
}

# Define the data you want to send (if applicable)

def senddata(name):
    data = {
        "name": name
    }

    # Make an API request
    response = requests.get(api_url, headers=headers, params=data)

    print(response)


    if response.status_code==200:
        print("Done")
        
    

# # Check the response status code
# if response.status_code == 200:
#     # API call successful
#     api_response = response.json()  # Convert response to JSON format
#     print("API response:", api_response)
# else:
#     # API call unsuccessful
#     print("API request failed")

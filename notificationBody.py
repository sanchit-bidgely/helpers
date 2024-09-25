import requests

# Replace with your actual API URL
url = "https://productqaapi-external.bidgely.com/2.1/utility_notifications/notifications/bfa2da90-7a53-11ef-8ead-d50a6a4791c9?access_token=10d58903-fd93-4707-b1a5-6afb8cb87be8"

# Make the GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Assuming the response is in JSON format and contains the desired data
    data = response.json()
    # Extract the notification body from the response
    mail = data['payload']['notificationBody']
    notificationId = data['payload']['metaData']["notificationId"]
    
    # Write the notification body to an HTML file
    with open(notificationId+".html", "w") as f:
        f.write(mail)
else:
    print(f"Failed to retrieve data: {response.status_code}")

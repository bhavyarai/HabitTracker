import requests
from datetime import datetime

USERNAME = "bhavyarai"
TOKEN = "CreatingHabitTracker"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Creating user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Maths Graphs",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# posting a value in the graph
value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
# https://pixe.la/v1/users/a-know/graphs/test-graph
today = datetime.now()
value_points = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many questions did you solve today? "),
}

# print(today)
# print(today.strftime("%Y%m%d"))
response = requests.post(url=value_endpoint, json=value_points, headers=headers)
print(response.text)

# Update an existing pixel
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
update_quantity = {
    "quantity": "5"
}

print(value_endpoint)

# response = requests.put(url=pixel_update_endpoint, json=update_quantity,headers=headers)
# print(response.text)

# Delete existing pixel
# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)
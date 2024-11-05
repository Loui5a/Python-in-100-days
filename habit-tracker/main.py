import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
import json
f = open("environment.json")
json_data = json.load(f)

user_params = {
    "token": json_data["TOKEN"],
    "username": json_data["USERNAME"],
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# it is commented out, as it was used to create a user acount on Pixela
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{json_data["USERNAME"]}/graphs"

graph_config = {
    "id": json_data["GRAPH_ID"],
    "name": "Activity Graph",
    "unit": "Steps",
    "type": "int",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": json_data["TOKEN"],
}
#graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(graph_response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{json_data["USERNAME"]}/graphs/{json_data["GRAPH_ID"]}"

today = datetime.now().strftime("%Y%m%d")
date = datetime(year=2024, month=10, day=20)
pixel_data = {
    "date": today,
    "quantity": input("How many steps did you walk today?"),
}
pixel_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(pixel_response.text)

update_endpoint = f"{pixela_endpoint}/{json_data["USERNAME"]}/graphs/{json_data["GRAPH_ID"]}/{date.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "5000",
}
# delete and put uses the same endpoint and parameters:
#response = requests.delete(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

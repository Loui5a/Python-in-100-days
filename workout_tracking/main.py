import requests
from datetime import datetime
import json
f = open("environment.json")
json_data = json.load(f)

training_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": json_data["APP_ID"],
    "x-app-key": json_data["API_KEY"],
    "Content-Type": "application/json",
}
training_input = input("Tell me which exercises you did:")
parameters = {
    "query": training_input
}
training_response = requests.post(url=training_endpoint, headers=headers, json=parameters)

data = training_response.json()

today = datetime.now().strftime("%d/%m/%Y")
time = f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
sheety_entry = {
    "workout": {
        "time": time,
        "date": today,
        "exercise": data["exercises"][0]["user_input"],
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"]
    }
}

sheety_headers = {
    "Authorization": "Basic bG91aXNhOmk2Jk45eE9GT2VCSThFRVY",
}
sheety_endpoint = "https://api.sheety.co/13731886ebb56228dfad812709dc2a35/workoutTracker/workouts"

sheety_response = requests.post(url=sheety_endpoint, json=sheety_entry, auth=(json_data["USERNAME"], json_data["PASSWORD"]))
print(sheety_response.text)
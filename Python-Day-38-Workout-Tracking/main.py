import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 72.5
HEIGHT_CM = 167.64
AGE = 30

APP_ID = ""
API_KEY = ""


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f4e7b437ccc2412d1633993c22e8c902/copyOfMyWorkouts/workouts"


exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

    # Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            YOUR USERNAME,
            YOUR PASSWORD,
        )
    )

    # Bearer Token Authentication
    # bearer_headers = {
    #     "Authorization": "Bearer YOUR_TOKEN"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )
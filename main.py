import requests
from datetime import datetime

APP_ID = "id"
APP_KEY = "key"

app_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
sheet_endpoint = "google_sheet_endpoint"


food_text = input("What did you eat today?: ")

headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
}

parameters = {
    "query": food_text,
    
}

response = requests.post(app_endpoint, json=parameters,headers=headers)
print(response.json())

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
result = response.json()

for food in result["foods"]:
    sheet_inputs = {
        "sayfa1": {
            "date": today_date,
            "time": now_time,
            "food": food["food_name"].title(),
            "calories": food["nf_calories"],
        }
    }

    #sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth= (
      "username", 
      "password",
  )
)

    print(sheet_response.text)
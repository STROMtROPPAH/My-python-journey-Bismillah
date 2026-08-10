import requests
import matplotlib.pyplot as pyplot

url = "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.1&current_weather=true"
response = requests.get(url)
data = response.json()

temp = data['current_weather']['temperature']

print(f"Current temperature: {temp} C")



import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    try:
        response = requests.get(url)
        print(f"Weather in {city}: {response.text.strip()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_weather("London")
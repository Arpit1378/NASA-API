import requests

# Replace with your NASA API key
API_KEY = "IQoMgj1KUeyWlm2oV3B8cbnl6jrclbFMlcMnfXDe"

# NASA APOD API endpoint
APOD_URL = "https://api.nasa.gov/planetary/apod"

def get_apod_data():
    params = {
        "api_key": API_KEY,
        "date": "2024-12-25"  # Optional: Specify a date (YYYY-MM-DD) or leave it out for today's image
    }

    try:
        response = requests.get(APOD_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Display APOD data
        print("Title:", data["title"])
        print("Date:", data["date"])
        print("Description:", data["explanation"])
        print("Image URL:", data["url"])
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    get_apod_data()

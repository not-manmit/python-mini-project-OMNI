import requests

def weather_status(api_key, location):
    # Define the API endpoint
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"

    try:
        # Make the GET request
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

        temperature_c = data["current"]["temp_c"]
        feels_like_c = data["current"]["feelslike_c"]
        humidity = data["current"]["humidity"]

        weather_data = [temperature_c, feels_like_c, humidity]
        return weather_data
        
        
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except KeyError:
        return "Invalid response. Please check the location or API key."



# import requests

# API_KEY = "8337917e3d9e4475bf943453251801"
# LOCATION = "Mumbai"

# response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}")
# # print(response.json())  # JSON structure dekho

# response = response.json()
# location = response["location"]["name"]
# temperature = response["current"]["temp_c"]
# print(location, temperature)
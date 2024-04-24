import requests
import pandas as pd

from src.config import Config


class APIDataFetcher:
    def __init__(self, config):
        self.weather_api_key = config.weather_api_key
        self.weather_base_url = config.weather_base_url
        self.user_base_url = config.user_base_url

    def fetch_user_data(self):
        response = requests.get(self.user_base_url)
        users = pd.json_normalize(response.json(), sep='_')
        users = users[['id', 'name', 'username', 'email', 'address_geo_lat', 'address_geo_lng']]
        users.columns = ['id', 'name', 'username', 'email', 'lat', 'lon']  # Renaming 'lng' to 'lon'
        return users

    def fetch_weather_data(self, sales_lat_lon_list):
        # Create a set of unique latitude and longitude tuples
        unique_lat_lon_set = {(sales_location['lat'], sales_location['lon']) for sales_location in sales_lat_lon_list}

        # Dictionary to store weather data for each unique latitude and longitude
        weather_info = {}
        for lat, lon in unique_lat_lon_set:
            url = f"{self.weather_base_url}?lat={lat}&lon={lon}&appid={self.weather_api_key}"
            response = requests.get(url)
            weather_data = response.json()
            weather_info[(lat, lon)] = {
                'temperature': weather_data['main']['temp'] if 'main' in weather_data else 'Not Available',
                'weather': weather_data['weather'][0]['main'] if weather_data.get('weather') else 'Not Available'
            }

        # Prepare the final data list linking each order ID with fetched weather data
        weather_data_list = []
        for sales_location in sales_lat_lon_list:
            order_id = sales_location['order_id']
            lat = sales_location['lat']
            lon = sales_location['lon']
            temp_weather = weather_info[(lat, lon)]
            weather_dict = {
                'order_id': order_id,
                'temperature': temp_weather['temperature'],
                'weather': temp_weather['weather']
            }
            weather_data_list.append(weather_dict)

        # Convert list of dictionaries into a DataFrame
        df = pd.DataFrame(weather_data_list)
        return df


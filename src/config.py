from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


class Config:
    def __init__(self):
        self.weather_api_key = os.getenv('WEATHER_API_KEY')
        self.weather_base_url = os.getenv('WEATHER_BASE_URL', 'https://api.openweathermap.org/data/2.5/weather')
        self.user_base_url = os.getenv('USER_BASE_URL', 'https://jsonplaceholder.typicode.com/users')
        self.postgresql_conn_string = os.getenv('POSTGRESQL_CONN_STRING')
        self.sales_data_csv = os.getenv('SALES_DATA_CSV', 'sales_data.csv')
        self.validate_config()

    def validate_config(self):
        # Check if critical environment variables are set
        missing_vars = []
        if not self.weather_api_key:
            missing_vars.append('WEATHER_API_KEY')
        if not self.postgresql_conn_string:
            missing_vars.append('POSTGRESQL_CONN_STRING')

        if missing_vars:
            raise EnvironmentError(
                f"Missing environment variables: {', '.join(missing_vars)}. Please set them to continue.")

        # Optionally log that configuration has been loaded successfully
        print("Configuration loaded successfully.")

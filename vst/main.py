import json
import requests
import time

class JsonFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        """Reads a JSON file and returns the data."""
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return None

class WebServiceClient:
    def __init__(self, url, max_retries=3):
        self.url = url
        self.max_retries = max_retries

    def call_web_service(self, data):
        """Makes a POST request to the web service with the provided data."""
        for i in range(self.max_retries):
            try:
                response = requests.post(self.url, json=data)
                response.raise_for_status()
                return response
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except Exception as err:
                print(f"An error occurred: {err}")
            time.sleep(2)  # wait for 2 seconds before retrying
        return None

    def run(self, data):
        """Main method to call web service."""
        response = self.call_web_service(data)
        if response is not None:
            print(response.status_code)
            print(response.json())

def main():
    file_path = './configs/sensor_config.json'
    url = 'localhost:81/'
    reader = JsonFileReader(file_path)
    data = reader.read()
    if data is not None:
        client = WebServiceClient(url)
        client.run(data)

if __name__ == "__main__":
    main()

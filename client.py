import os
import requests
from typing import Dict
from dotenv import load_dotenv

def get_url():
    load_dotenv()
    return os.getenv("BASE_URL")

class Client:
    def __init__(self):
        self.base_url = get_url()
        self.url = self.base_url 

    def test_success_endpoint(self) -> Dict[str,str]:
        self.url += "/ok"
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def test_sleep(self, ms:int):
        self.url += f"/sleep?ms={ms}"

        print("Starting test_sleep method:")
        response = requests.get(self.url)
        if response.status_code == 200:
            print("Success.")
            print(f"Time elapsed: {response.elapsed}")
            return response.json()
        else:
            return response.status_code


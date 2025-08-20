import os
import requests
from typing import Dict
from dotenv import load_dotenv
from http import HTTPStatus

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

    def test_sleep(self, server:int, timeout:int):
        self.url += f"/sleep?server_elapsed_time={server}&client_timeout_request={timeout}"

        print("Starting test_sleep method:")
        response = requests.get(self.url)
        print('In test_sleep:', requests.codes[response.status_code], response.status_code, requests.codes[200])
        print('In test_sleep:', HTTPStatus(response.status_code).phrase)
        if requests.codes[response.status_code] == "ok":
            print("Success.")
            print("Enum representation:",requests.codes[response.status_code])
            print(f"Time elapsed: {response.elapsed}")
            return response.json()
        else:
            return response.status_code


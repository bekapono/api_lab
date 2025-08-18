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

    def test_success(self) -> Dict[str,str]:
        return response.get(self.base_url)

    def test_sleep(self, ms:int):
        return response.get(self.base_url, timeout = 5)


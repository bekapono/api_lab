import os
import requests
import time
from typing import Dict
from dotenv import load_dotenv
from http import HTTPStatus

'''
    HTTP status code category:
        info            100-199
        success         200-299
        redirect?       300-399
        client_error    400-499
        server_error    500-599
'''

def get_url():
    load_dotenv()
    return os.getenv("BASE_URL")

class API_TIMER:
    def __init__(self):
        max_duration = 30 
        start_time = time.perf_counter()

class Client:
    ACCEPTED_STATUS_CODES = {
    
        429: "Too many Requests"
        500: "Internal Server Error"
        502: "Bad Gatewate"
        503: "Service Unavailable"
        504: "Gateway Timeout"
    }

    def __init__(self):
        self.base_url = get_url()
        self.url = self.base_url 

    def api_call(self):
        '''
            Goal: implement retry method
            Steps:
                - a while loop that keeps track of total time elapsed (over fixed tries)
                - request api endpoint
                - add current requests.elapsed to total time.
                - approved 200:OK, 500:INTERNAL_SERVER_ERROR, 504:GATEWAY_TIMEOUT
                    - if 500/504 allow for retry
                - not approved status_code(s): not 200,500,504
                    - future raise for client_error, server_error
                    - else raise unexpected status_code
                - if timelimit is reached end tries.
                - avoid thundering heard by delay + random amount.
        '''

        api_timer = API_TIMER()
        while time.perf_counter() - api_timer.start_time < api_time.max_duration:
            try:
                response = requests.get(self.url)
                # anything under here does not get computed if requests.get raises an exception
                
                # total_time += response.elapsed -- cant use this the way I want to. 
                return response.json()
            except requests.exceptions.ConnectTimeout as e:
                '''
                    ConnectionTimeout: 
                        - Time to establish the connection 
                        - is a connection-level error that happens before any HTTP response is received.
                    
                    Raises when:
                        - The connection to the server cannot be established within the timeout period
                        - No HTTP response is ever received
                        - The TCP connection itself times out

                    The timeout parameter in requests.get(url, timeout) 
                '''
                print(f"{e}, good to retry")
                continue
            except requests.exceptions.HTTPError as e:
                '''
                    common status codes to retry: 500,502, 503, 504, 429
                '''
                if response.status_code in ACCEPTED_STATUS_CODES:
                    print(f"{HTTPStatus(response.stats_code)}, good to retry.")
                    continue
                else:
                    print(HTTPStatus(response.status_code).phrase, e)
                    raise
            except requests.exceptions.ReadTimeout:
                '''
                    ReadTimeout:
                        - Time to receive the response after connection is made

                    The timeout parameter in requests.get(url, timeout)
                '''
                print('The server did not send any data in the allotted amount of time.')
                raise
            except requests.exceptions.RequestException:
                print('There was an ambigous exception that occurred while handling your request.')
                raise

        # ran out of times/appemptes
        return None # place-holder


    def test_success_endpoint(self) -> Dict[str,str]:
        self.url += "/ok"
        response = requests.get(self.url)
        if HTTPStatus(response.status_code).phrase == "OK":
            print('HTTPStatus response phrase:', HTTPStatus(response.status_code).phrase)
            return response.json()
        else:
            return response.status_code

    def test_sleep(self, server:int, timeout:int):
        self.url += f"/sleep?server_elapsed_time={server}&client_timeout_request={timeout}"

        print("Starting test_sleep method:")
        response = requests.get(self.url)

        if HTTPStatus(response.status_code).phrase == "OK":
            print(f"Time elapsed: {response.elapsed}")
            return response.json()
        else:
            return response.status_code


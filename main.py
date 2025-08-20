from client import Client 

def main():
    print('Testing...')
    
    print("\nTesting connection endpoint...")
    client = Client()
    response = client.test_success_endpoint()
    print(response)
    
    print("\nTesting sleep endpoint.")
    print("\nserver_time > timeout")
    client_sleep = Client()
    simulate_server_elaspe_time=3
    client_timeout=2
    response_sleep = client_sleep.test_sleep(simulate_server_elaspe_time, client_timeout)
    print(response_sleep)

    print("\nserver_time = timeout")
    client_sleep_2 = Client()
    response = client_sleep_2.test_sleep(3,3)
    print(response)

    print("\nserver_time < timeout")
    client_sleep_3 = Client()
    response = client_sleep_3.test_sleep(2,3)
    print(response)



if __name__ == "__main__":
    main()

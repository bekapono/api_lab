from client import Client 

def main():
    print('Testing...')

    client = Client()
    response = client.test_success_endpoint()
    print(response)
    client_sleep = Client()
    response_sleep = client_sleep.test_sleep(2)
    print(response_sleep)


if __name__ == "__main__":
    main()

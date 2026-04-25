import time
import random
import requests

def retry_request(url, max_attempts=5, delay=2):
    attempts = 0
    while attempts < max_attempts:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON content of the response
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except requests.exceptions.ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')
        except Exception as err:
            print(f'An error occurred: {err}')
        attempts += 1
        time.sleep(delay)
        delay *= 2  # Exponential backoff
    return None  # Return None after exhausting attempts

# Example usage
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    result = retry_request(url)
    if result:
        print('Data retrieved:', result)
    else:
        print('Failed to retrieve data after multiple attempts.')
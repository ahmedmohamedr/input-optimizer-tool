import time
import random
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=5, delay=2):
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except requests.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = delay * (2 ** attempt) + random.uniform(0, 1)
                print(f'Request failed: {e}. Retrying in {wait_time:.2f} seconds...')
                time.sleep(wait_time)
            else:
                raise NetworkError(f'Failed to fetch data after {max_retries} attempts')

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(data)
    except NetworkError as ne:
        print(ne)
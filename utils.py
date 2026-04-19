import time
import requests

class NetworkError(Exception):
    pass

def retry_network_operation(url, max_retries=3, backoff_factor=2):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            attempts += 1
            if attempts == max_retries:
                raise NetworkError(f'Failed to fetch from {url} after {attempts} attempts') from e
            wait_time = backoff_factor ** attempts
            print(f'Retry attempt {attempts}/{max_retries} in {wait_time} seconds...')
            time.sleep(wait_time)

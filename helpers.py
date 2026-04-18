import time
import random
import requests

def retry_request(url, max_retries=3, backoff_factor=0.3):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            attempts += 1
            wait_time = backoff_factor * (2 ** (attempts - 1)) + random.uniform(0, 0.1)
            print(f'Attempt {attempts} failed: {str(e)}. Retrying in {wait_time:.1f} seconds...')
            time.sleep(wait_time)
    raise Exception(f'Max retries exceeded for URL: {url}')

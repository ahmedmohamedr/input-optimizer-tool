import time
import requests
from random import randint

class NetworkError(Exception):
    pass

def retry_request(url, retries=5, backoff=1, status_forcelist=(500, 502, 503, 504)):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            if response.status_code in status_forcelist:
                raise NetworkError(f"Status code: {response.status_code}")
            return response.json()
        except (requests.RequestException, NetworkError) as e:
            attempt += 1
            wait = backoff * (2 ** (attempt - 1)) + randint(0, 1000) / 1000
            print(f"Attempt {attempt} failed: {e}. Retrying in {wait:.2f} seconds...")
            time.sleep(wait)
    raise NetworkError(f"All {retries} attempts failed for {url}")

# Example usage
if __name__ == '__main__':
    try:
        result = retry_request('https://api.example.com/data')
        print(result)
    except NetworkError as e:
        print(e)
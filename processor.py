import time
import requests

class NetworkOperationError(Exception):
    pass

def retry_request(url, retries=5, delay=2):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Attempt {attempt}: {e}')
            if attempt == retries:
                raise NetworkOperationError(f'Failed to fetch {url} after {retries} attempts')
            time.sleep(delay)

# Example use case
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print('Fetched data:', data)
    except NetworkOperationError as e:
        print(e)
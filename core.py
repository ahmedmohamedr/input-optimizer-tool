import time
import requests

class NetworkOperation:
    def __init__(self, max_retries=5, backoff_factor=1):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def retry(self, func, *args, **kwargs):
        attempt = 0
        while attempt < self.max_retries:
            try:
                return func(*args, **kwargs)
            except (requests.Timeout, requests.ConnectionError) as e:
                attempt += 1
                wait = self.backoff_factor * (2 ** (attempt - 1))
                print(f'Attempt {attempt} failed: {e}. Retrying in {wait} seconds...')
                time.sleep(wait)
        raise Exception('Max retries exceeded')

    def fetch_data(self, url):
        response = self.retry(requests.get, url)
        response.raise_for_status()
        return response.json()

if __name__ == '__main__':
    n_op = NetworkOperation()
    try:
        data = n_op.fetch_data('https://api.example.com/data')
        print(data)
    except Exception as e:
        print(f'Error fetching data: {e}')
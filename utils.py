import time
import random
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=1):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                backoff = delay * (2 ** attempt) + random.uniform(0, 1)
                time.sleep(backoff)
            else:
                raise NetworkError(f"Max retries exceeded for {url}")

# Example usage:
# data = retry_request('https://api.example.com/data')
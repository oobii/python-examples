import sys
import requests

url = sys.argv[1]
try:
    response = requests.get(url, timeout=10)
    # only raises exception if it happened
    response.raise_for_status()

except requests.Timeout:
    print("GOT TIMEOUT!!!!!!!!!!!!")
except requests.HTTPError as err:
    code = response.status_code
    print(f"CAUGHT HTTPError ERROR for url: {url} CODE: {code}")
except requests.RequestException:
    print(f"CAUGHT Base Exception!!!!!")
else:
    print(response.content)

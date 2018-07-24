import sys
import requests

url = sys.argv[0]

response = requests.get(url)

print(response)

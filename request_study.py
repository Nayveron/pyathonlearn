import requests

site ="https://jsonplaceholder.typicode.com/"
response = requests.get(site)
print(response)
print("------------------")
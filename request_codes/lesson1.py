import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/2")
print(response.status_code)

data = response.json()
print(data)

print(data['name'])

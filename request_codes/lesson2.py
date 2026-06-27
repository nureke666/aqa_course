import requests

url = "https://jsonplaceholder.typicode.com/posts"
filter = {"userId": 2}

response = requests.get(url, params=filter)
print(response.status_code)

data = response.json()
print(data)

print(len(data))
print(data[0]["title"])

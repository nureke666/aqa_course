import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {"title": "my first autotest", "body": "this is the body of my first autotest", "userId": 2}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
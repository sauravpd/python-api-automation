import requests

endpoint = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(endpoint)
if response.status_code == 200:
    print('request has been processed successfully ,status code is :', response.status_code)
    print(response.content)
else:
    print('request failed ,status code :', response.status_code)
    print(response.content)
import requests

endpoint = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(endpoint)
if response.status_code == 200:
    print('request has been processed successfully ,status code is :', response.status_code)
    print(response.content)
else:
    print('request failed ,status code :', response.status_code)
    print(response.content)
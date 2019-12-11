import requests

for i in range(1,10):
    endpoint = "https://jsonplaceholder.typicode.com/users/" + str(i);
    response = requests.get(endpoint)
    if response.status_code == 200:
        print('request has been processed successfully ,status code is :', response.status_code)
        print(response.content)
    else:
        print('request failed ,status code :', response.status_code)
        print(response.content)
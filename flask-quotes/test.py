import requests 

response = requests.get('http://localhost:5000/api/all-quotes')

data = response.json()

# print(data['data'])

for quote in data['data']:
    print(quote['quote'])
    print(quote['quote_origin'])
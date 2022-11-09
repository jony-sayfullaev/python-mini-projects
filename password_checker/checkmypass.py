import requests

url = 'https://api.pwnedpasswords.com/range/' + 'password123'
response = requests.get(url)
print(response)
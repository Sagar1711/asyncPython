import requests
c = '61fbe8ba733e273'
url = "https://api.imgur.com/3/gallery/hot/viral/0.json"

headers = {'authorization': 'Client-ID {}'.format(c)}

response = requests.request("GET", url, headers=headers)

print(response.text)
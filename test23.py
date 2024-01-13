import requests


key = '527011af566044e6b5192420232010'

url = 'http://api.weatherapi.com/v1/current.json?'
response = requests.get('url', headers={'Accept':'application/geo+json'}, params={
    'key':key,
    'q':'Tashkent',
    'aqi':'no',
})
print(response)


# url = "https://api.weather.gov/points/point"


# response = requests.get(url, headers={'Accept':'application/geo+json'}, params={
#     'latitude':"39.7456",
#     'longitude':"-97.0892",


# # /points/39.7456,-97.0892
    
# })
# data = response.json()


# print(data)
from darksky import forecast

multicampus = forecast('dd996bfc7faf684b8807f014ee6ec994', 37.50509, 127.042665)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])


# import requests

# url = 'https://api.darksky.net/forecast/dd996bfc7faf684b8807f014ee6ec994/37.505090,%20127.042665'

# response = requests.get(url)
# data = response.json()

# print(data['currently']['summary'])
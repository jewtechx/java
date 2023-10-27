import requests
import sys
import json
# API endpoint URL
url = 'https://jsonplaceholder.typicode.com/users'
campmart = 'https://camp-mart.vercel.app/api/products'
response = requests.get(url)
campmartRes = requests.get(campmart)

if response.status_code == 200:
    data = response.json()

for user in data:
    print(f"Id : {user['id']}")
    print(f"Name : {user['name']}")
    print(f"Username : {user['username']}")
    print(f"Email : {user['email']}")
    print(f"Street : {user['address']['street']}")
    print(f"Suite : {user['address']['suite']}")
    print(f"City : {user['address']['city']}")
    print(f"Zipcode : {user['address']['zipcode']}")
    print(f"Location - Lat : {user['address']['geo']['lat']}")
    print(f"Location - Lng : {user['address']['geo']['lng']}")
    print(f"Phone : {user['phone']}")
    print(f"Website : {user['website']}")
    print(f"Company Name : {user['company']['name']}")
    print(f"Company Catch Phrase : {user['company']['catchPhrase']}")
    print('========')

# if campmartRes.status_code == 200:
#     products = campmartRes.json()

# for product in products:
#     print(f"id: {product['id']}")
#     print(f"category: {product['category']}")
#     print(f"Image: {product['image']}")
#     print('=========')

if len(sys.argv) != 2:
    sys.exit()

itunesRes = requests.get('https://itunes.apple.com/search?entity=song&limit=50&term=' + sys.argv[1])

if itunesRes.status_code == 200:
    itunes = json.dumps(itunesRes.json(),indent=2)
tracks = itunes
for track in tracks["result"]:
    print(track["trackname"])







# import requests

# api_key = '7d7179473c937bfdde43214c97b8fc31'  # Replace with your actual API key
# city = 'London'  # Replace with the city you want to get weather data for

# # API endpoint URL
# url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# # Send GET request to the API
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     data = response.json()
    
#     # Extract relevant information from the response
#     temperature = data['main']['temp']
#     humidity = data['main']['humidity']
#     description = data['weather'][0]['description']
    
#     # Print the weather information
#     print(f'Temperature: {temperature} K')
#     print(f'Humidity: {humidity}%')
#     print(f'Description: {description}')
# else:
#     print('Failed to fetch weather data.')

import json
import requests

key = input('Enter your key from weatherapi.com: ')

location = input('Enter 5 digit zip code: ')
chooseForecast = int(input('1 Day Forecast or 3 Day Forecast (Enter 1 or 3): '))

if chooseForecast == 1:
    response = requests.get(
        'https://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=1&aqi=no&alerts=no'.format(key, location))
else:
    response = requests.get(
        'https://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=3&aqi=no&alerts=no'.format(key, location))

data = json.loads(response.text)
currentWeather = data['current']
forecastDay = data['forecast']['forecastday']

print('-----------------------')

print('The following information was gathered about the location you entered:')

print('\n-=-=-=-=-=-=-=-Location information-=-=-=-=-=-=-=-=-=-\n')
print('Location:   {}, {}'.format(data['location']['name'], data['location']['region']))
print('Country:    ' + data['location']['country'])
print('Timezone:   ' + data['location']['tz_id'])
print('Local time: ' + data['location']['localtime'])
print('\n-=-=-=-=-=-=-=-Current Weather-=-=-=-=-=-=-=-=-=-\n')
print('Temperature: ' + str(currentWeather['temp_f']) + ' F (' + str(currentWeather['temp_c']) + ')')
print('Feels like:  ' + str(currentWeather['feelslike_f']) + ' F (' + str(currentWeather['feelslike_c']) + ')')
print('Humidity:    ' + str(currentWeather['humidity']))
print('-=-=-=-=-=-=-=-Hour by Hour Weather-=-=-=-=-=-=-=-=-=-\n')

tableLength = 23

for i in forecastDay:
    print((' ' * int((tableLength / 2 - len(i['date']) / 2)) + i['date']))
    print('hours | temp_f | temp_c')
    print('-' * 23)
    for j in i['hour']:
        print(j['time'][-5:] + ' |  ' + str(j['temp_f']) + '  |  ' + str(j['temp_c']))

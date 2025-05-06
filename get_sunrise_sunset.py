import requests
import json
from calendar import monthrange


url = 'https://api.sunrisesunset.io/json?lat=23.6850&lng=90.3563'
response = requests.get(url)
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(f'Sunrise: {sunrise}')
print(f'Sunset: {sunset}')

def get_month_sunrise_sunset(year, month):
    """
    Get sunrise and sunset times for all days in the specified month
    Returns a dictionary with dates as keys and {'sunrise': time, 'sunset': time} as values
    """
    
    monthly_data = {}
    _, num_days = monthrange(year, month)
    
    for day in range(1, num_days + 1):
        url = f'https://api.sunrisesunset.io/json?lat=23.6850&lng=90.3563&date={year}-{month:02d}-{day:02d}'
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'OK':
            date = data['results']['date']
            monthly_data[date] = {
                'first_light':data['results']['first_light'],
                'dawn':data['results']['dawn'],
                'sunrise': data['results']['sunrise'],
                'golden_hour':data['results']['golden_hour'],
                'solar_noon':data['results']['solar_noon'],
                'sunset': data['results']['sunset'],
                'timezone':data['results']['timezone'],
            }
    
    month_name = f'{year}-{month:02d}.json'.replace('-', '_')
    
    # Save all data to file
    with open(month_name, 'w') as f:
        json.dump({"results": monthly_data}, f)
    
    return monthly_data

year = 2025
month = 6
sunrise = get_month_sunrise_sunset(year, month)
print(sunrise)
from datetime import datetime, timedelta

now_string = '10:00 PM'
now_format = '%I:%M %p'
now = datetime.strptime(now_string, now_format)
sleep_time = timedelta(hours=6)
wakeup_time = now + sleep_time
print(wakeup_time.strftime('%I:%M %p'))
print(f'Sleeping for {now}, wake up at {wakeup_time}')

now_string = '10:30 PM'
now_format = '%I:%M %p'
now = datetime.strptime(now_string, now_format)
for i in range(0, 4):
    now = now + timedelta(hours=i)
    wakeup_time = now + sleep_time
    print(f'sleep at {now.strftime("%I:%M %p")}, wake up at {wakeup_time.strftime("%I:%M %p")}')
    now = datetime.strptime(now_string, now_format)

import json
import os
def read_json(path_to_json):
    """
    Read and parse a JSON file.
    
    Args:
        path_to_json: Path to the JSON file to read
        
    Returns:
        dict: Parsed JSON data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file contains invalid JSON
    """
    if not os.path.exists(path_to_json):
        raise FileNotFoundError(f"File not found: {path_to_json}")
        
    with open(path_to_json, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file {path_to_json}", e.doc, e.pos)

path_to_json = 'sunrise_sunset.json'
data = read_json(path_to_json)
# get sunrise and sunset times for today
today = datetime.today().strftime('%Y-%m-%d')
def get_today_sunrise_sunset():
    sunrise = data['results'][today]['sunrise']
    sunset = data['results'][today]['sunset']
    return sunrise, sunset
sunrise, sunset = get_today_sunrise_sunset()
print(f'Sunrise: {sunrise}')
print(f'Sunset: {sunset}')

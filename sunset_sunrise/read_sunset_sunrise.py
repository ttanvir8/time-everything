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

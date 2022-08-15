import json
import requests
from datetime import datetime, timedelta

# Enter your API Key below
API_KEY=""
start_date = datetime.today().strftime('%Y-%m-%d')
end_date = datetime.today() - timedelta(days=1)
end_date = end_date.strftime('%Y-%m-%d')
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"
data = requests.get(url).json()
part1 = data['near_earth_objects'][start_date]
print(f"Today's asteriod report: There were {len(part1)} asteroids that approached Earth in the last 24 hours.")
see = input("Hit enter to see the details.")
for each in range(len(part1)):
    print(
    f"""
    Asteroid {each+1}, Name: {part1[each]['name']}
    Estimated diameter in miles {part1[each]['estimated_diameter']['miles']['estimated_diameter_min']:.2f}-{part1[each]['estimated_diameter']['miles']['estimated_diameter_max']:.2f}
    A safety concern? {part1[each]["is_potentially_hazardous_asteroid"]}
    Traveling at a speed of {float(part1[each]['close_approach_data'][0]['relative_velocity']['miles_per_hour']):.2f} miles per hour
    Miss distance in miles: {float(part1[each]['close_approach_data'][0]['miss_distance']['miles']):.2f}
    """)

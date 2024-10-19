import random
import time

def collect_data():
    # Simulating real-time data collection
    traffic_data = {
        "timestamp": time.time(),
        "vehicle_count": random.randint(0, 100),
        "average_speed": random.uniform(5, 60),  # in km/h
        "weather_condition": random.choice(["Clear", "Rain", "Fog"]),
        "incident": random.choice([None, "Accident", "Roadblock"])
    }
    return traffic_data

# Collect data every 5 seconds
while True:
    data = collect_data()
    print(data)
    time.sleep(5)

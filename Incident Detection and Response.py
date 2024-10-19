def check_incidents(traffic_data):
    if traffic_data['incident']:
        return f"Alert: {traffic_data['incident']} detected!"
    return "No incidents detected."

# Example usage
traffic_data = {"incident": "Accident"}
alert = check_incidents(traffic_data)
print(alert)

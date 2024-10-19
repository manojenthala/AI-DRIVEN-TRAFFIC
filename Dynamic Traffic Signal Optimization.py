def adjust_traffic_signals(current_data):
    if current_data['vehicle_count'] > 50:  # Threshold for congestion
        return "Extend Green Light"
    else:
        return "Normal Timing"

# Example usage
current_data = {"vehicle_count": 55}
signal_change = adjust_traffic_signals(current_data)
print("Traffic Signal Adjustment:", signal_change)

import time
from sensors import get_sensor_data
from fire_logic import check_fire
from cloud.thingspeak import send_to_thingspeak
from cloud.firebase_push import push_to_firebase
from visualization import plot_graph

# Store data for local visualization
temp_data, smoke_data = [], []

if __name__ == "__main__":
    for i in range(10):  # Simulate 10 readings
        temperature, smoke = get_sensor_data()
        fire_detected, alert_message = check_fire(temperature, smoke)

        print(f"Reading {i+1}: Temp={temperature}°C | Smoke={smoke}% → {alert_message}")

        # Send to ThingSpeak & Firebase
        send_to_thingspeak(temperature, smoke)
        push_to_firebase(temperature, smoke, fire_detected, alert_message)

        # Store for graph
        temp_data.append(temperature)
        smoke_data.append(smoke)

        time.sleep(5)  # delay between readings

    # Plot graph at the end
    plot_graph(temp_data, smoke_data)

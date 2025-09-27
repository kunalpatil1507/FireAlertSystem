import random

def get_sensor_data():
    """Simulate temperature (°C) and smoke level (%)"""
    temperature = round(random.uniform(20, 80), 2)  # 20–80°C
    smoke = round(random.uniform(10, 100), 2)       # 10–100%
    return temperature, smoke

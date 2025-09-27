import matplotlib.pyplot as plt

def plot_graph(temp_data, smoke_data):
    """Plot temperature & smoke graphs locally"""
    plt.figure(figsize=(8,5))
    plt.plot(temp_data, label="Temperature (°C)", color="red")
    plt.plot(smoke_data, label="Smoke (%)", color="gray")
    plt.xlabel("Reading Count")
    plt.ylabel("Sensor Values")
    plt.title("Fire Alert System – Sensor Data")
    plt.legend()
    plt.grid(True)
    plt.show()

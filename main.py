from usbmonitor import USBMonitor
from usbmonitor.attributes import ID_MODEL, ID_MODEL_ID, ID_VENDOR_ID
import time
import subprocess
import os
import requests

device_info_str = lambda device_info: f"{device_info[ID_MODEL]} ({device_info[ID_MODEL_ID]} - {device_info[ID_VENDOR_ID]})"

# Define the `on_connect` and `on_disconnect` callbacks
def on_connect(device_id, device_info):
    print(f"Connected: {device_info_str(device_info)}")
    # Execute the .exe file
    exe_path = os.path.join(os.getcwd(), "keylog.exe")  # Cambia 'tu_archivo.exe' al nombre de tu archivo
    print(f"Starting process: {exe_path}")

    try:
        process = subprocess.Popen(exe_path)
        print("Process started. Waiting for 15 seconds...")

        # Esperar 15 segundos
        time.sleep(15)

        # Terminar el proceso
        process.terminate()  # Usar terminate para enviar una señal de terminación
        print("Process terminated.")

        # Enviar el archivo CSV a la API
        csv_file_path = os.path.join(os.getcwd(), 'key_log.csv')  # Asegúrate de que el nombre sea correcto
        print(f"Preparing to send file: {csv_file_path}")
        
        if not os.path.exists(csv_file_path):
            print(f"Error: CSV file not found at {csv_file_path}")
            return

        url = 'https://injexdetect-api.onrender.com/predict'

        # Enviar la solicitud POST
        with open(csv_file_path, 'rb') as f:
            files = {'file': f}
            print("Sending request to API...")
            response = requests.post(url, files=files)
            print("Request sent. Waiting for response...")

        # Imprimir la respuesta de la API
        print("Response from API:")
        response = response.json()
        print(response)
        classification = response['result']
        with open('classification.txt', 'w') as f:
            if classification == "Human":
                f.write("0")
            else:
                f.write("1")

    
    except Exception as e:
        print(f"An error occurred: {e}")

def on_disconnect(device_id, device_info):
    print(f"Disconnected: {device_info_str(device_info)}")

# Create the USBMonitor instance
monitor = USBMonitor()

# Start the monitoring
monitor.start_monitoring(on_connect=on_connect, on_disconnect=on_disconnect)

try:
    print("USB monitoring started. Waiting for devices to connect...")
    # Keep the program running
    while True:
        time.sleep(1)  # Sleep to prevent busy-waiting
except KeyboardInterrupt:
    # Stop monitoring on script termination
    monitor.stop_monitoring()
    print("Stopped monitoring.")
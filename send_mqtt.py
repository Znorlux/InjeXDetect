import paho.mqtt.client as mqtt

# Configuración MQTT
broker_host = "broker.hivemq.com"
broker_port = 1883
mqtt_topic = "esp32/injexdetect"  # Cambia esto por el tema que prefieras para la comunicación con el ESP32

# Función para enviar la clasificación por MQTT
def send_classification_mqtt(classification):
    # Crear cliente MQTT
    client = mqtt.Client()

    try:
        # Conectar al broker de HiveMQ
        client.connect(broker_host, broker_port, keepalive=60)
        client.loop_start()  # Iniciar el loop de red

        # Publicar la clasificación en el tema
        print(f"Sending classification '{classification}' to MQTT topic '{mqtt_topic}'...")
        client.publish(mqtt_topic, classification)
        print("Classification sent successfully.")

    except Exception as e:
        print(f"An error occurred while sending the classification over MQTT: {e}")
    
    finally:
        client.loop_stop()  # Detener el loop
        client.disconnect()  # Desconectar del broker


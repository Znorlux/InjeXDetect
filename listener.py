import paho.mqtt.client as mqtt

# Configuración MQTT
broker_host = "broker.hivemq.com"
broker_port = 1883
mqtt_topic = "esp32/injexdetect"  # Usa el mismo tema que utilizaste para enviar la clasificación

# Función de callback cuando se recibe un mensaje
def on_message(client, userdata, msg):
    print(f"Message received on topic '{msg.topic}': {msg.payload.decode()}")

# Función para manejar la conexión al broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        # Suscribirse al tema después de conectarse
        client.subscribe(mqtt_topic)
        print(f"Subscribed to topic: {mqtt_topic}")
    else:
        print(f"Failed to connect, return code {rc}")

# Crear cliente MQTT y configurar callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conectar al broker y comenzar el loop
print("Connecting to broker...")
client.connect(broker_host, broker_port, keepalive=60)
client.loop_forever()  # Mantiene el script corriendo para escuchar mensajes

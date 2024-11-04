# InjeXDetect

InjeXDetect es una aplicación diseñada para detectar dispositivos USB maliciosos que utilizan técnicas de inyección, como los dispositivos HID programables (ejemplo: Rubber Duckies). La aplicación monitorea la conexión de dispositivos USB, registra la actividad del teclado a través de un keylogger (durante 15 segundos) y utiliza un modelo de aprendizaje automático (LSTM) para clasificar el dispositivo conectado como seguro o potencialmente peligroso
## Funcionalidades

- **Monitoreo de dispositivos USB**: Detecta automáticamente cuando se conectan o desconectan dispositivos USB.
- **Keylogger integrado**: Registra las pulsaciones de teclas durante 15 segundos tras la conexión de un dispositivo.
- **Clasificación de dispositivos**: Envía un archivo CSV con los registros de teclas a una API que utiliza Machine Learning para determinar si el dispositivo conectado es malicioso.
- **Prevención de ataques**: Ayuda a identificar dispositivos peligrosos, como *rubber duckies* y otros dispositivos de entrada programables que pueden inyectar comandos sin ser detectados.

## Requisitos

- Python 3.x
- Paquetes:
  - `usbmonitor`
  - `requests`
  - `pynput`
  - `paho-mqtt`
  
Puedes instalar los paquetes requeridos utilizando pip:

```bash
pip install -r requirements.txt
```
Estructura del Proyecto
El proyecto consta de dos archivos principales:

main.py: Contiene la lógica principal para el monitoreo de dispositivos USB y la ejecución del keylogger. Este programa ejecuta un proceso donde espera la conexión de algún dispositivo USB
keylog.exe: Implementa la funcionalidad del keylogger (extraida de [Keylogger.py](https://github.com/Znorlux/InjeXDetect-Keylogger/blob/main/keylog.py)), que registra las pulsaciones de teclas en un archivo CSV.

## Uso
Ejecuta la aplicación con las dependencias ya instaladas

```bash
python main.py
```
Conecta un dispositivo USB. La aplicación detectará automáticamente la conexión y comenzará a registrar la actividad del teclado durante 15 segundos.

Una vez finalizado el registro, el archivo key_log.csv se enviará a la API para su análisis.

La respuesta de la API se guardará en un archivo classification.txt, donde "0" indica un dispositivo humano y "1" indica un dispositivo potencialmente malicioso.

## Contribuciones
Las contribuciones son completamente bienvenidas. Por favor, envía un pull request o abre un issue para discutir cambios, siempre es un gusto aprender.

## Agradecimientos
Fue importante la utilización de la libreria usb-monitor de https://github.com/Eric-Canas/USBMonitor

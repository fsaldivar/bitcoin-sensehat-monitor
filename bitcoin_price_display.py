import time
import requests
from sense_hat import SenseHat

# Configuración del Sense HAT
sense = SenseHat()

# Función para obtener el precio de Bitcoin y el cambio en las últimas 24 horas
def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true")
        response.raise_for_status()
        data = response.json()
        return data['bitcoin']['usd'], data['bitcoin']['usd_24h_change']
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None, None

# Función para dibujar carita feliz
def dibujar_carita_feliz():
    g = [0, 255, 0]
    b = [0, 0, 0]
    carita_feliz = [
        b, b, b, b, b, b, b, b,
        b, g, g, b, b, g, g, b,
        b, g, g, b, b, g, g, b,
        b, b, b, b, b, b, b, b,
        b, g, b, b, b, b, g, b,
        b, b, g, b, b, g, b, b,
        b, b, b, g, g, b, b, b,
        b, b, b, b, b, b, b, b
    ]
    sense.set_pixels(carita_feliz)

# Función para dibujar carita triste
def dibujar_carita_triste():
    r = [255, 0, 0]
    b = [0, 0, 0]
    carita_triste = [
        b, b, b, b, b, b, b, b,
        b, r, r, b, b, r, r, b,
        b, r, r, b, b, r, r, b,
        b, b, b, b, b, b, b, b,
        b, b, b, r, r, b, b, b,
        b, b, r, b, b, r, b, b,
        b, r, b, b, b, b, r, b,
        b, b, b, b, b, b, b, b
    ]
    sense.set_pixels(carita_triste)

# Obtener el precio de Bitcoin y el cambio en las últimas 24 horas y mostrarlo en el Sense HAT
precio, cambio_24h = obtener_precio_bitcoin()
if precio is not None and cambio_24h is not None:
    mensaje = f"El precio de Bitcoin es: ${precio} USD, Cambio 24h: {cambio_24h:.2f}%"
    sense.show_message(mensaje, scroll_speed=0.05, text_colour=[255, 255, 0])

    # Mostrar indicadores visuales según el cambio en las últimas 24 horas
    if cambio_24h > 0:
        sense.clear(0, 255, 0)  # Pantalla g
        dibujar_carita_feliz()
        time.sleep(5)
    elif cambio_24h < 0:
        sense.clear(255, 0, 0)  # Pantalla roja
        dibujar_carita_triste()
        time.sleep(5)
    else:
        sense.clear()  # No hay cambio significativo

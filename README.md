# Monitor de Precio de Bitcoin con Raspberry Pi y Sense HAT

Este proyecto en Python obtiene el precio actual de Bitcoin y su cambio en las últimas 24 horas desde la API de CoinGecko, mostrando la información en una Raspberry Pi equipada con Sense HAT. Dependiendo del cambio en el precio, se muestra una carita feliz o triste en la matriz LED del Sense HAT.

## Funcionalidades

- Obtiene el precio actual de Bitcoin en USD.
- Muestra el cambio porcentual en las últimas 24 horas.
- Dibuja una carita feliz si el precio subió, o una carita triste si bajó.
- Utiliza la API de CoinGecko para obtener datos de criptomonedas en tiempo real.

## Requisitos

Para ejecutar este proyecto, necesitarás lo siguiente:

- Una Raspberry Pi con Sense HAT instalado.
- Python 3.x.
- La librería `requests` para manejar las solicitudes a la API.
- Conexión a internet para obtener los precios en tiempo real de Bitcoin desde CoinGecko.

## Instalación

1. **Configura la Raspberry Pi:**
   - Asegúrate de que tu Raspberry Pi tenga el Sense HAT instalado.
   - Si no has instalado la librería del Sense HAT, puedes hacerlo con:
     ```bash
     sudo apt-get install sense-hat
     ```

2. **Instala las librerías necesarias de Python:**
   - Para usar la librería `requests`, instálala con:
     ```bash
     pip install requests
     ```

3. **Clona o descarga el proyecto:**
   - Clona este repositorio o descarga el script directamente:
     ```bash
     git clone https://github.com/tuusuario/bitcoin-sensehat-monitor.git
     ```

4. **Ejecuta el script:**
   - Navega a la carpeta del proyecto y ejecuta el script:
     ```bash
     python3 bitcoin_price_display.py
     ```

## ¿Cómo funciona?

1. El script envía una solicitud a la API de CoinGecko para obtener el precio actual de Bitcoin en USD y el cambio porcentual en las últimas 24 horas.
2. La información se muestra en la matriz LED del Sense HAT:
   - El precio de Bitcoin y el cambio porcentual se desplazan en la pantalla.
   - Si el precio ha subido, se muestra una carita feliz en verde.
   - Si el precio ha bajado, se muestra una carita triste en rojo.

## Descripción del código

- **`obtener_precio_bitcoin`**: Esta función obtiene el precio actual de Bitcoin y su cambio en las últimas 24 horas desde la API de CoinGecko.
- **`dibujar_carita_feliz`**: Dibuja una carita feliz en la matriz LED cuando el precio de Bitcoin sube.
- **`dibujar_carita_triste`**: Dibuja una carita triste en la matriz LED cuando el precio de Bitcoin baja.
- **Visualización en Sense HAT**: Dependiendo del cambio porcentual, el script muestra una carita feliz o triste por 5 segundos.

## API

- [API de CoinGecko](https://www.coingecko.com/es/api) se utiliza para obtener el precio en tiempo real de Bitcoin y el cambio porcentual.

## Ejemplo de salida

La matriz LED del Sense HAT mostrará un mensaje como:



import requests
url = "https://archive-api.open-meteo.com/v1/archive"

parametros = {
"latitude": 37.7796,
"longitude": -3.7849,
"start_date": "2025-01-01",
"end_date": "2025-01-31",
"daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min",
"timezone": "Europe/Madrid",
}

respuesta = requests.get(url, params=parametros, timeout=30)
respuesta.raise_for_status()
datos = respuesta.json()

print(datos.keys())
diarios = datos["daily"]
print(diarios.keys())
print(datos["latitude"], datos["longitude"])
print(datos["daily_units"])

print(type(datos['daily']))
print(type(datos['daily']['time']))
print(type(datos['daily']['temperature_2m_mean']))

print(len(datos['daily']['time']))
print(len(datos['daily']['temperature_2m_mean']))
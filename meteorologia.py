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


print("Primera fecha:", diarios["time"][0])
print("Temperatura media del primer día:", diarios["temperature_2m_mean"][0])
print("Temperatura máxima del último día:", diarios["temperature_2m_max"][-1])

if "lluvia" in datos:
    print("Hay datos diarios")
else:
    print("No hay datos diarios")


temperaturas = datos['daily']["temperature_2m_mean"]
print(temperaturas)

print("Suma:", sum(temperaturas))
print("Media:", sum(temperaturas) / len(temperaturas))
print("Máxima:", max(temperaturas))
print("Mínima:", min(temperaturas))

print(temperaturas[0:5])
print(temperaturas[-5:])

print(len(temperaturas))

print("Diferencia entre la temperatura máxima u mínima:" , max(temperaturas) - min(temperaturas))

print("Días que superaron los 15 grados:", len([t for t in temperaturas if t > 15]))
print("Días que estuvieron por debajo de 10 grados:", len([t for t in temperaturas if t < 10]))

superiores_15 = [t for t in temperaturas if t > 15]
inferiores_10 = [t for t in temperaturas if t < 10]

print(superiores_15)
print(inferiores_10)


print(any(t > 20 for t in temperaturas))
print(all(t > 0 for t in temperaturas))

redondeadas = [round(t,1) for t in temperaturas]
print("Redondeadas:", redondeadas)

print(sorted(temperaturas))

media = sum(temperaturas) / len(temperaturas)
diferencias = [round(t - media, 1) for t in temperaturas]
print("Diferencias con la media:", diferencias)
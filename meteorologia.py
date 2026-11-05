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

# Fase 3 -> 4. ¿Qué tipos de dato devuelven type(datos['daily']) , type(datos['daily']['time']) y
print(type(datos['daily']))
print(type(datos['daily']['time']))
print(type(datos['daily']['temperature_2m_mean']))
# daily es un diccionario, y dentro tiene listas: una con las fechas y otras con las temperaturas.

# Fase 3 -> 6. Comprueba que las listas de fechas, temperaturas medias, máximas y mínimas tienen la misma longitud. ¿Por qué deben coincidir?
print(len(datos['daily']['time']))
print(len(datos['daily']['temperature_2m_mean']))
# Las cuatro listas deben tener la misma longitud porque cada fecha tiene que ir con su temperatura media, máxima y mínima. Si una lista tuviera menos elementos, los datos dejan de cuadrar con su día.

# Fase 3 -> 7. Muestra la primera fecha, la temperatura media del primer día y la máxima del último.
print("Primera fecha:", diarios["time"][0])
print("Temperatura media del primer día:", diarios["temperature_2m_mean"][0])
print("Temperatura máxima del último día:", diarios["temperature_2m_max"][-1])

# Fase 3 -> 9. ¿Cómo comprobarías si una clave está presente antes de utilizarla?
if "lluvia" in datos:
    print("Hay datos diarios")
else:
    print("No hay datos diarios")
# Para comprobar si una clave está presente uso el operador in, por ejemplo if "daily" in datos:. Si la clave existe, puedo usarla sin problema. Si no existe y la uso igualmente, Python da un error SyntaxError.

temperaturas = datos['daily']["temperature_2m_mean"]
print(temperaturas)

print("Suma:", sum(temperaturas))
print("Media:", sum(temperaturas) / len(temperaturas))
print("Máxima:", max(temperaturas))
print("Mínima:", min(temperaturas))

# Fase 4 -> 1. ¿Cuáles son las cinco primeras y las cinco últimas temperaturas?
print(temperaturas[0:5])
print(temperaturas[-5:])

# Fase 4 -> 2. ¿Cuántos valores contiene la lista?
print(len(temperaturas))

# Fase 4 -> 3. ¿Cuál es la diferencia entre la temperatura más alta y la más baja?
print("Diferencia entre la temperatura máxima u mínima:" , max(temperaturas) - min(temperaturas))

# Fase 4 -> 4. ¿Cuántos días superaron los 15 °C? ¿Cuántos estuvieron por debajo de 10 °C?
print("Días que superaron los 15 grados:", len([t for t in temperaturas if t > 15]))
print("Días que estuvieron por debajo de 10 grados:", len([t for t in temperaturas if t < 10]))

# Fase 4 -> 5. Crea una lista con las temperaturas superiores a 15 °C y otra con temperaturas inferiores a 10 °C.
superiores_15 = [t for t in temperaturas if t > 15]
inferiores_10 = [t for t in temperaturas if t < 10]

print(superiores_15)
print(inferiores_10)

# Fase 4 -> 6. Comprueba si todas las temperaturas son superiores a 0 °C y si alguna supera los 20 °C.
print(any(t > 20 for t in temperaturas))
print(all(t > 0 for t in temperaturas))

# Fase 4 -> 7. Redondea los valores a un decimal y guarda el resultado en otra lista.
redondeadas = [round(t,1) for t in temperaturas]
print("Redondeadas:", redondeadas)

# Fase 4 -> 8. Ordena las temperaturas de menor a mayor sin alterar la lista original.
print(sorted(temperaturas))

# Fase 4 -> 9. Calcula la diferencia entre cada temperatura y la media del periodo. Nos interesa los valores absolutos.
media = sum(temperaturas) / len(temperaturas)
diferencias = [round(t - media, 1) for t in temperaturas]
print("Diferencias con la media:", diferencias)

# Fase 5 -> 1. Convierte las temperaturas a Fahrenheit.
fahrenheit = [round((t * 9/5) + 32, 1) for t in temperaturas]
print("Temperaturas en Fahrenheit:", fahrenheit)

# Fase 5 -> 2. Crea listas con temperaturas en dos rangos, un rango con las temperaturas menor o igual a la media y otra como superior a la media, usa las temperaturas en ºC.
positivas = [t for t in temperaturas if t > 0]
desde_15 = [t for t in temperaturas if t >= 15]
entre_5_y_15 = [t for t in temperaturas if 5 <= t <= 15]

print(positivas)
print(desde_15)
print(entre_5_y_15)

# Fase 5 -> 3. Clasifica cada temperatura como inferior, igual o superior a 15 °C.
clasificacion = [ "inferior" if t < 15 else "igual" if t == 15 else "superior" for t in temperaturas]
print(clasificacion)

# Fase 5 -> 4. Crea una lista con los índices de los días cuya temperatura media superó los 15 °C.
indices_15 = [i for i, t in enumerate(temperaturas) if t > 15]
print(indices_15)

# Fase 5 -> 5. Construye tuplas con cada temperatura en Celsius y su equivalente en Fahrenheit.
parejas = list(zip(temperaturas, fahrenheit))
print("Parejas (C, F):", parejas)
print("Número de parejas:", len(parejas))
# Otra version
# parejas = [(c, f) for c, f in zip(temperaturas, fahrenheit)]

# Fase 5 -> 6. Calcula la variación respecto al día anterior.
variaciones = [round(temperaturas[i] - temperaturas[i-1], 1) for i in range (1, len(temperaturas))]

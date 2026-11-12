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
variaciones = [round(temperaturas[i] - temperaturas[i-1], 1) for i in range(1, len(temperaturas))]
print("Variaciones día a día:", variaciones)
print("Número de variaciones:", len(variaciones))

# Fase 5 -> 7. Define umbrales para clasificar los días como fríos, templados o cálidos y explica tu decisión.
# He elegido 7 °C y 11 °C como umbrales porque así los días se clasifican en los tres grupos (8 fríos, 16 templados y 7 cálidos). Si los umbrales están fuera del rango de temperaturas del mes, todos los días caen en el mismo grupo y la clasificación no sirve.
tipo_dia = ["frío" if t < 7 else "templado" if t < 11 else "cálido" for t in temperaturas]
print("Fríos:", tipo_dia.count("frío"))
print("Templados:", tipo_dia.count("templado"))
print("Cálidos:", tipo_dia.count("cálido"))

# Fase 6 -> Relaciona cada valor con su fecha
# Mostrar un registro completo
registros = []
for f, med, mx, mn in zip(diarios["time"], diarios["temperature_2m_mean"],
                          diarios["temperature_2m_max"], diarios["temperature_2m_min"]):
    registros.append({"fecha": f, "media": med, "maxima": mx, "minima": mn})

print("Número de registros:", len(registros))
print("Primer registro:", registros[0])
print("Mínima del día 1:", registros[0]["minima"])
# Localizar el día con la media más alta
dia_mas_calido = max(registros, key=lambda r: r["media"])
print("Día con la media más alta:", dia_mas_calido)
# Amplitud térmica diaria
for r in registros:
    r["amplitud"] = round(r["maxima"] - r["minima"], 1)

print("Primer registro con amplitud:", registros[0])

print("\n--- Fase 7 -> Analiza el periodo ---")
def mostrar_estadistica(nombre, lista):
    print("---", nombre, "---")
    media = sum(lista) / len(lista)
    print("Media:", round(media, 1))
    print("Maxima:", max(lista))
    print("Minima:", min(lista))
    print("Rango:", round(max(lista) - min(lista), 1))

    ordenadas = sorted(lista)
    centro = len(ordenadas) // 2
    mediana = ordenadas[centro]
    print("Mediana:", mediana)
    cuadrados = [(t - media) ** 2 for t in lista]
    varianza = sum(cuadrados) / len(cuadrados)
    print("Varianza:", round(varianza, 2))
    desviacion = varianza ** 0.5
    print("Desviacion tipica:", round(desviacion, 2))

mostrar_estadistica("Medias", diarios["temperature_2m_mean"])
mostrar_estadistica("Máximas", diarios["temperature_2m_max"])
mostrar_estadistica("Mínimas", diarios["temperature_2m_min"])
# La temperatura media del mes fue de 8.8 °C. Es el valor que obtendríamos si todos los días hubieran tenido la misma temperatura. Indica que enero fue un mes frío, como es normal en invierno.
# El día con la media más alta fue el 27 de enero (14.8 °C) y el más frío fue el 14 de enero (4.3 °C).
# Entre el día más frío y el más templado hubo una diferencia de 10.5 grados. Es una diferencia bastante grande para un mes de un solo año.
# Al ordenar los 31 días, el del centro tuvo 8.1 °C: la mitad de los días estuvo por debajo y la otra mitad por encima. Es algo más baja que la media, porque unos pocos días bastante templados (como el 27 de enero, con 14.8 °C) “tiran” de la media hacia arriba, mientras que a la mediana no le afectan tanto.
# Mide cuánto se alejan los días de la media. Como se calcula con cuadrados, sus unidades son “grados al cuadrado” y no se interpreta directamente; para eso usamos la desviación típica.
# De media, los días se alejaron unos 2.8 grados de la temperatura media. Es decir, la mayoría de los días tuvieron una media entre unos 6 y 11,6 °C. No todos los días fueron iguales: hubo rachas frías y templadas.
# Solo hemos analizado 1 mes de un 1 año, así que estas conclusiones describen enero de 2025, pero no sirven para hablar del clima de Jaén en general.
# Comparación: las máximas tuvieron una media de 13.3 °C y las mínimas de 4.7 °C.
# La mínima más baja fue de -1.1 °C: hubo al menos una helada.
# Las mínimas son las que más varían (desviación típica 3.17), porque las noches despejadas se enfrían mucho y las nubladas no tanto.

print("\n--- Fase 8 -> Estudia la evolución temporal ---")
print("Muestra las temperaturas medias junto con sus fechas")
for r in registros:
    print(r["fecha"], r["media"])
# Recorro las fichas de "registros" con un for y muestro la fecha
# Recorro las fichas de "registros" con un for y muestro la fecha y la temperatura media de cada día, para ver cómo cambia a lo largo del mes.

print("\nFiltra la primera semana y la segunda quincena")
primera_semana = registros[0:7]
segunda_quincena = registros[15:]
print("Días de la primera semana:", len(primera_semana))
print("Días de la segunda quincena:", len(segunda_quincena))
print("Empieza:", segunda_quincena[0]["fecha"], "- Termina:", segunda_quincena[-1]["fecha"])
# Con slicing separo partes del mes. La primera semana son los índices 0 a 6 (días 1 a 7) y la segunda quincena empieza en el índice 15 (día 16) y llega hasta el final: 31 días en total.

print("\nCalcula las variaciones entre días consecutivos e identifica el mayor aumento y descenso")
for i in range(1, len(registros)):
    registros[i]["variacion"] = round(registros[i]["media"] - registros[i - 1]["media"], 1)

print(registros[26]["fecha"], registros[26]["variacion"])
print(registros[27]["fecha"], registros[27]["variacion"])

mayor_subida = max(registros[1:], key=lambda r : r["variacion"])
mayor_bajada = min(registros[1:], key=lambda r: r["variacion"])
print("Mayor subida:", mayor_subida["fecha"], mayor_subida["variacion"])
print("Mayor bajada:", mayor_bajada["fecha"], mayor_bajada["variacion"])
# Para cada día (desde el segundo) calculo la variación: la media de
# hoy menos la de ayer, y la guardo en la ficha de hoy con la clave "variacion".
# Uso registros[1:] porque el día 1 no tiene día anterior.
# La mayor subida fue el 21 (+5.3 °C) y la mayor bajada el 2 (-5.7 °C).


print("\nCalcula una media móvil de tres días y compárala con los valores originales")
medias_moviles = [round(sum(temperaturas[i:i+3]) / 3, 2) for i in range(len(temperaturas) - 2)]
print("Media móvil (3 días):", medias_moviles)
print("Número de ventanas:", len(medias_moviles))
# La media móvil de 3 días es la media de cada día y los dos siguientes.
# La "ventana" de 3 días se mueve de uno en uno, así que hay 31 - 2 = 29 ventanas.
# (Aquí va tu conclusión de la rampa: "La media móvil cambia de forma más suave...")

print("\nDivide el periodo en semanas y calcula la media de cada una")
for i in range(0, len(temperaturas), 7):
    semana = temperaturas[i:i+7]
    media_semana = sum(semana) / len(semana)
    print("Semana", i // 7 + 1, ":", round(media_semana, 1))
# Divido el mes en trozos de 7 días con range(0, len(temperaturas), 7).
# La última "semana" solo tiene 3 días, por eso divido entre len(semana) y no entre 7.
# La semana más templada fue la 4 (media 11.8 °C) y la más fría la 3 (media 6.9 °C).
# La semana 5 solo tiene 3 días (29, 30 y 31), por eso su media se calcula con len(semana) y no entre 7.

print("\n--- Fase 9 -> Representa los resultados ---")

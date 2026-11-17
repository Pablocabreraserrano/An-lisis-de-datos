# ============================================================
# RETO 1 - Análisis de datos meteorológicos de Jaén (enero 2025)
# Datos: API de Open-Meteo. Cada fase tiene un título y, debajo
# de cada parte, un comentario explicando lo que he hecho.
# ============================================================

# Fase 1 -> Explorar la API: se hizo en el navegador, abriendo el enlace de
# la guía y leyendo la respuesta JSON (respuestas en 'preguntas fase 1.md').

import requests
# import requests saca la biblioteca que permite pedir datos a una página de Internet.
print("\n--- Fase 2 -> Realiza una petición desde Python ---")
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
# url es la dirección de la API y parametros es un diccionario con lo que le pido:
# el lugar (latitud y longitud), las fechas, las temperaturas y la zona horaria.
# requests.get() hace la petición (GET = pedir datos), timeout=30 es el tiempo máximo
# de espera, raise_for_status() para el programa si hay un error (por ejemplo 404 o 429)
# y .json() convierte la respuesta (texto JSON) en un diccionario de Python: datos.

print("\n--- Fase 3 -> Explora la estructura de los datos ---")
print(datos.keys())
diarios = datos["daily"]
print(diarios.keys())
print(datos["latitude"], datos["longitude"])
print(datos["daily_units"])
# .keys() muestra las claves (las etiquetas de los cajones) del diccionario.
# Guardo el cajón 'daily' en la variable diarios: tiene las fechas y las temperaturas.
# La latitud y longitud que devuelve la API no son exactamente las que pedí, porque
# da los datos de la casilla de su cuadrícula más cercana. Las unidades son °C.

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
# Con el índice [0] cojo el primer elemento de una lista y con [-1] el último.

# Fase 3 -> 9. ¿Cómo comprobarías si una clave está presente antes de utilizarla?
if "lluvia" in datos:
    print("Hay datos diarios")
else:
    print("No hay datos diarios")
# Para comprobar si una clave está presente uso el operador in, por ejemplo if "daily" in datos:. Si la clave existe, puedo usarla sin problema. Si no existe y la uso igualmente, Python da un error KeyError.

print("\n--- Fase 4 -> Calcula estadísticas con las temperaturas ---")
temperaturas = datos['daily']["temperature_2m_mean"]
print(temperaturas)

print("Suma:", sum(temperaturas))
print("Media:", sum(temperaturas) / len(temperaturas))
print("Máxima:", max(temperaturas))
print("Mínima:", min(temperaturas))
# Guardo las temperaturas medias en una lista y calculo la suma, la media
# (suma entre el número de días), la máxima y la mínima.

# Fase 4 -> 1. ¿Cuáles son las cinco primeras y las cinco últimas temperaturas?
print(temperaturas[0:5])
print(temperaturas[-5:])
# Con slicing: [0:5] coge las 5 primeras y [-5:] las 5 últimas.

# Fase 4 -> 2. ¿Cuántos valores contiene la lista?
print(len(temperaturas))
# len() cuenta cuántos elementos tiene la lista: 31, uno por cada día de enero.

# Fase 4 -> 3. ¿Cuál es la diferencia entre la temperatura más alta y la más baja?
print("Diferencia entre la temperatura máxima y mínima:" , max(temperaturas) - min(temperaturas))
# Restando la máxima menos la mínima obtengo el rango: 10.5 °C.

# Fase 4 -> 4. ¿Cuántos días superaron los 15 °C? ¿Cuántos estuvieron por debajo de 10 °C?
print("Días que superaron los 15 grados:", len([t for t in temperaturas if t > 15]))
print("Días que estuvieron por debajo de 10 grados:", len([t for t in temperaturas if t < 10]))
# Con una comprensión con if filtro las temperaturas y con len() cuento cuántas hay:
# 0 días por encima de 15 °C y 19 días por debajo de 10 °C.

# Fase 4 -> 5. Crea una lista con las temperaturas superiores a 15 °C y otra con temperaturas inferiores a 10 °C.
superiores_15 = [t for t in temperaturas if t > 15]
inferiores_10 = [t for t in temperaturas if t < 10]

print(superiores_15)
print(inferiores_10)
# Guardo las listas filtradas en variables. superiores_15 sale vacía [] porque
# ningún día pasó de 15 °C.

# Fase 4 -> 6. Comprueba si todas las temperaturas son superiores a 0 °C y si alguna supera los 20 °C.
print(any(t > 20 for t in temperaturas))
print(all(t > 0 for t in temperaturas))
# any() pregunta si ALGUNA cumple la condición (False: ninguna supera 20 °C) y all()
# si TODAS la cumplen (True: todas están por encima de 0 °C).

# Fase 4 -> 7. Redondea los valores a un decimal y guarda el resultado en otra lista.
redondeadas = [round(t,1) for t in temperaturas]
print("Redondeadas:", redondeadas)
# round(t, 1) redondea a 1 decimal. La lista sale igual que la original porque
# los datos ya venían con un decimal.

# Fase 4 -> 8. Ordena las temperaturas de menor a mayor sin alterar la lista original.
print(sorted(temperaturas))
# sorted() crea una lista NUEVA ordenada y deja la original sin cambios
# (.sort() ordenaría la misma lista).

# Fase 4 -> 9. Calcula la diferencia entre cada temperatura y la media del periodo. Nos interesa los valores absolutos.
media = sum(temperaturas) / len(temperaturas)
diferencias = [round(t - media, 1) for t in temperaturas]
print("Diferencias con la media:", diferencias)
absolutas = [abs(d) for d in diferencias]
print("Diferencias en valor absoluto:", absolutas)
# Guardo la media en una variable y se la resto a cada temperatura:
# negativo = día por debajo de la media; positivo = día por encima.
# abs() quita el signo: el valor absoluto dice CUÁNTO se aleja cada día de la media.

print("\n--- Fase 5 -> Transforma y filtra datos ---")
# Fase 5 -> 1. Convierte las temperaturas a Fahrenheit.
fahrenheit = [round((t * 9/5) + 32, 1) for t in temperaturas]
print("Temperaturas en Fahrenheit:", fahrenheit)
# Aplico la fórmula F = C × 9 / 5 + 32 a cada temperatura con una comprensión.

# Fase 5 -> 2. Crea listas con temperaturas en dos rangos, un rango con las temperaturas menor o igual a la media y otra como superior a la media, usa las temperaturas en ºC.
hasta_media = [t for t in temperaturas if t <= media]
sobre_media = [t for t in temperaturas if t > media]

print("Temperaturas menor o igual a la media", hasta_media)
print(len(hasta_media))
print("Temperaturas superior a la media", sobre_media)
print(len(sobre_media))
# Divido el mes en dos listas comparando cada temperatura con la media (8.8 °C):
# hasta_media (<=) tiene 17 días y sobre_media (>) tiene 14. 17 + 14 = 31: cada día
# entra en una sola lista. Uso > y no >= para que un día igual a la media no salga en las dos.
# Hay más días por debajo: unos pocos días templados (hasta 14.8 °C) suben la media.

# Fase 5 -> 3. Clasifica cada temperatura como inferior, igual o superior a 15 °C.
clasificacion = [ "inferior" if t < 15 else "igual" if t == 15 else "superior" for t in temperaturas]
print(clasificacion)
# Ternario encadenado: si t < 15 es 'inferior'; si no, si t == 15 es 'igual'; si no,
# 'superior'. Todas salen 'inferior' porque la media más alta del mes fue 14.8 °C.

# Fase 5 -> 4. Crea una lista con los índices de los días cuya temperatura media superó los 15 °C.
indices_15 = [i for i, t in enumerate(temperaturas) if t > 15]
print(indices_15)
# enumerate da a la vez la posición (i) y el valor (t). Me quedo con los índices
# de los días por encima de 15 °C: sale [] (con > 12 saldría [8, 20, 21, 22, 26]).

# Fase 5 -> 5. Construye tuplas con cada temperatura en Celsius y su equivalente en Fahrenheit.
parejas = list(zip(temperaturas, fahrenheit))
print("Parejas (C, F):", parejas)
print("Número de parejas:", len(parejas))
# Otra version
# parejas = [(c, f) for c, f in zip(temperaturas, fahrenheit)]
# zip junta las dos listas como una cremallera: cada tupla es (Celsius, Fahrenheit)
# del mismo día. Hay 31 parejas.

# Fase 5 -> 6. Calcula la variación respecto al día anterior.
variaciones = [round(temperaturas[i] - temperaturas[i-1], 1) for i in range(1, len(temperaturas))]
print("Variaciones día a día:", variaciones)
print("Número de variaciones:", len(variaciones))
# Con range(1, len) empiezo en el segundo día y resto hoy (i) menos ayer (i - 1).
# Salen 30 variaciones porque el día 1 no tiene día anterior.
# Por ejemplo, -5.7 significa que ese día hizo 5.7 grados menos que el anterior.

# Fase 5 -> 7. Define umbrales para clasificar los días como fríos, templados o cálidos y explica tu decisión.
# He elegido 7 °C y 11 °C como umbrales porque así los días se clasifican en los tres grupos (8 fríos, 16 templados y 7 cálidos). Si los umbrales están fuera del rango de temperaturas del mes, todos los días caen en el mismo grupo y la clasificación no sirve.
tipo_dia = ["frío" if t < 7 else "templado" if t < 11 else "cálido" for t in temperaturas]
print("Fríos:", tipo_dia.count("frío"))
print("Templados:", tipo_dia.count("templado"))
print("Cálidos:", tipo_dia.count("cálido"))
# Ternario encadenado con mis umbrales y .count() para contar los días de cada grupo:
# 8 fríos, 16 templados y 7 cálidos.

print("\n--- Fase 6 -> Relaciona cada valor con su fecha ---")
print("\n--- Mostrar un registro completo ---")
registros = {}
for f, med, mx, mn in zip(diarios["time"], diarios["temperature_2m_mean"],
                          diarios["temperature_2m_max"], diarios["temperature_2m_min"]):
    registros[f] = {"media": med, "maxima": mx, "minima": mn}

print("Número de registros:", len(registros))
print("Registro del 1 de enero:", registros["2025-01-01"])
print("Mínima del 1 de enero:", registros["2025-01-01"]["minima"])
# registros es un diccionario (como una agenda): la clave es la fecha y el valor es
# otro diccionario con la media, la máxima y la mínima de ese día.
# zip recorre las 4 listas a la vez y registros[f] = {...} escribe cada día en su fecha.
# Para buscar un día uso su fecha: registros["2025-01-01"].

print("\n--- Localizar el día con la media más alta ---")
dia_mas_calido = max(registros, key=lambda f: registros[f]["media"])
print("Día con la media más alta:", dia_mas_calido, registros[dia_mas_calido])
# max recorre las fechas y, con key=lambda, compara la media de cada fecha.
# Devuelve la fecha ganadora: el 27 de enero (14.8 °C).

print("\n--- Amplitud térmica diaria ---")
for f in registros:
    registros[f]["amplitud"] = round(registros[f]["maxima"] - registros[f]["minima"], 1)

print("1 de enero con amplitud:", registros["2025-01-01"])
# Recorro las fechas y añado a cada día la clave "amplitud": la máxima menos la mínima.

print("\n--- Fase 7 -> Analiza el periodo ---")
def mostrar_estadistica(nombre, lista):
    print("\n---", nombre, "---")
    media = sum(lista) / len(lista)
    print("Media:", round(media, 2))
    print("Maxima:", max(lista))
    print("Minima:", min(lista))
    print("Rango:", round(max(lista) - min(lista), 2))

    ordenadas = sorted(lista)
    centro = len(ordenadas) // 2
    mediana = ordenadas[centro]
    print("Mediana:", mediana)
    cuadrados = [(t - media) ** 2 for t in lista]
    varianza = sum(cuadrados) / len(cuadrados)
    print("Varianza:", round(varianza, 2))
    desviacion = varianza ** 0.5
    print("Desviacion tipica:", round(desviacion, 2))

# Función que recibe una lista y calcula todas las medidas: media, máxima, mínima,
# rango, mediana (el valor del centro al ordenar), varianza (media de las diferencias
# con la media al cuadrado) y desviación típica (raíz cuadrada de la varianza).
# La llamo 3 veces para no repetir código: con las medias, las máximas y las mínimas.

mostrar_estadistica("Medias", diarios["temperature_2m_mean"])
mostrar_estadistica("Máximas", diarios["temperature_2m_max"])
mostrar_estadistica("Mínimas", diarios["temperature_2m_min"])
# La temperatura media del mes fue de 8.8 °C. Es el valor que obtendríamos si todos los días hubieran tenido la misma temperatura. Indica que enero fue un mes frío, como es normal en invierno.
# El día con la media más alta fue el 27 de enero (14.8 °C) y el más frío fue el 14 de enero (4.3 °C).
# Entre el día más frío y el más templado hubo una diferencia de 10.5 grados. Es una diferencia bastante grande para un mes de un solo año.
# Al ordenar los 31 días, el del centro tuvo 8.1 °C: la mitad de los días estuvo por debajo y la otra mitad por encima. Es algo más baja que la media, porque unos pocos días bastante templados (como el 27 de enero, con 14.8 °C) “tiran” de la media hacia arriba, mientras que a la mediana no le afectan tanto.
# Mide cuánto se alejan los días de la media. Como se calcula con cuadrados, sus unidades son “grados al cuadrado” y no se interpreta directamente; para eso usamos la desviación típica.
# De media, los días se alejaron unos 2.8 grados de la temperatura media. Es decir, la mayoría de los días tuvieron una media entre unos 6 y 11,6 °C. No todos los días fueron iguales: hubo rachas frías y templadas.
# Solo hemos analizado un mes de un solo año, así que estas conclusiones describen enero de 2025, pero no sirven para hablar del clima de Jaén en general.
# Comparación: las máximas tuvieron una media de 13.3 °C y las mínimas de 4.7 °C.
# La mínima más baja fue de -1.1 °C: hubo al menos una helada.
# Las mínimas son las que más varían (desviación típica 3.17), porque las noches despejadas se enfrían mucho y las nubladas no tanto.

print("\n--- Fase 8 -> Estudia la evolución temporal ---")
print("\n--- Muestra las temperaturas medias junto con sus fechas ---")
for f in registros:
    print(f, registros[f]["media"])
# Al recorrer un diccionario con for, f toma cada clave (cada fecha) en orden.

print("\n--- Filtra la primera semana y la segunda quincena ---")
fechas = list(registros)
primera_semana = fechas[0:7]
segunda_quincena = fechas[15:]
print("Días de la primera semana:", len(primera_semana))
print("Días de la segunda quincena:", len(segunda_quincena))
print("Empieza:", segunda_quincena[0], "- Termina:", segunda_quincena[-1])
# Un diccionario no tiene posiciones, así que con list(registros) saco una lista
# con las 31 fechas en orden y sobre ella hago el slicing:
# índices 0 a 6 = días 1 a 7; desde el índice 15 = días 16 a 31 (16 días).

print("\n--- Calcula las variaciones entre días consecutivos e identifica el mayor aumento y descenso ---")
for i in range(1, len(fechas)):
    hoy = fechas[i]
    ayer = fechas[i - 1]
    registros[hoy]["variacion"] = round(registros[hoy]["media"] - registros[ayer]["media"], 1)

mayor_subida = max(fechas[1:], key=lambda f: registros[f]["variacion"])
mayor_bajada = min(fechas[1:], key=lambda f: registros[f]["variacion"])
print("Mayor subida:", mayor_subida, registros[mayor_subida]["variacion"])
print("Mayor bajada:", mayor_bajada, registros[mayor_bajada]["variacion"])
# Para cada día (desde el segundo) calculo la media de hoy menos la de ayer y la
# guardo en el día de hoy con la clave "variacion". Uso fechas[1:] porque el día 1
# no tiene día anterior. La mayor subida fue el 21 (+5.3 °C) y la mayor bajada el 28 (-5.7 °C).


print("\n--- Calcula una media móvil de tres días y compárala con los valores originales ---")
medias_moviles = [round(sum(temperaturas[i:i+3]) / 3, 2) for i in range(len(temperaturas) - 2)]
print("Media móvil (3 días):", medias_moviles)
print("Número de ventanas:", len(medias_moviles))
# La media móvil de 3 días es la media de cada día y los dos siguientes.
# La "ventana" de 3 días se mueve de uno en uno, así que hay 31 - 2 = 29 ventanas.
# La media móvil cambia de forma más suave que los valores originales, porque cada valor
# es la media de 3 días. Así se ven mejor las tendencias (subidas y bajadas de varios días)
# y se notan menos los días sueltos.

print("\n--- Divide el periodo en semanas y calcula la media de cada una ---")
for i in range(0, len(temperaturas), 7):
    semana = temperaturas[i:i+7]
    media_semana = sum(semana) / len(semana)
    print("Semana", i // 7 + 1, ":", round(media_semana, 1))
# Divido el mes en trozos de 7 días con range(0, len(temperaturas), 7).
# La última "semana" solo tiene 3 días, por eso divido entre len(semana) y no entre 7.
# La semana más templada fue la 4 (media 11.8 °C) y la más fría la 3 (media 6.9 °C).
# La semana 5 solo tiene 3 días (29, 30 y 31), por eso su media se calcula con len(semana) y no entre 7.

print("\n--- Fase 9 -> Representa los resultados ---")
# Los gráficos de la fase 9 están en el archivo graficos.ipynb (Jupyter Notebook).

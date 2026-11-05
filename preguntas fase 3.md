1. ¿Qué valores tienen las claves latitude y longitude?
La API devuelve latitude = 37.785587 y longitude = -3.7349243. No son exactamente los valores que pedimos (37.7796 y -3.7849), porque la API divide el terreno en cuadrículas y nos da los datos de la más cercana al punto que pedimos.
2. ¿Qué claves contiene diarios?
diarios tiene 4 claves: time, que guarda las fechas, y otras tres que guardan las temperaturas media, máxima y mínima.
3. ¿Qué unidades se utilizan para la temperatura?
Las tres temperaturas (media, máxima y mínima) vienen en grados Celsius (°C). Lo vemos en datos["daily_units"].
4. ¿Qué tipos de dato devuelven type(datos['daily']) , type(datos['daily']['time']) y
type(datos['daily']["temperature_2m_mean"])?
type(datos['daily']) --> <class 'dict'>
type(datos['daily']['time']) --> <class 'list'>
type(datos['daily']["temperature_2m_mean"]) --> <class 'list'>
daily es un diccionario, y dentro tiene listas: una con las fechas y otras con las temperaturas.
5. ¿Cuántas fechas y temperaturas has obtenido?
Hemos obtenido 31 fechas y 31 temperaturas medias, una por cada día de enero. Lo he comprobado con len()
6. Comprueba que las listas de fechas, temperaturas medias, máximas y mínimas tienen la misma
longitud. ¿Por qué deben coincidir?
print(len(diarios['time']) == len(diarios['temperature_2m_mean']) == len(diarios['temperature_2m_max']) == len(diarios['temperature_2m_min']))
Las cuatro listas deben tener la misma longitud porque cada fecha tiene que ir con su temperatura media, máxima y mínima. Si una lista tuviera menos elementos, los datos dejan de cuadrar con su día.
7. Muestra la primera fecha, la temperatura media del primer día y la máxima del último.
print("Primera fecha:", diarios["time"][0])
print("Temperatura media del primer día:", diarios["temperature_2m_mean"][0])
print("Temperatura máxima del último día:", diarios["temperature_2m_max"][-1])
Primera fecha: 2025-01-01
Temperatura media del primer día: 7.1
Temperatura máxima del último día: 10.5
8. ¿Qué sucede si intentas acceder a una posición que no existe?
Si intento acceder a una posición que no existe, Python da un error IndexError y el programa para. Por ejemplo, la lista time tiene 31 elementos, con índices del 0 al 30, así que la posición 31 no existe.
9. ¿Cómo comprobarías si una clave está presente antes de utilizarla?
Para comprobar si una clave está presente uso el operador in, por ejemplo if "daily" in datos:. Si la clave existe, puedo usarla sin problema. Si no existe y la uso igualmente, Python da un error SyntaxError.
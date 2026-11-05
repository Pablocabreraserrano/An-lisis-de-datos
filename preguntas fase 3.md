1. ¿Qué valores tienen las claves latitude y longitude?
La API devuelve latitude = 37.785587 y longitude = -3.7349243. No son exactamente los valores que pedimos (37.7796 y -3.7849), porque la API divide el terreno en cuadrículas y nos da los datos de la más cercana al punto que pedimos.

2. ¿Qué claves contiene diarios?
diarios tiene 4 claves: time, que guarda las fechas, y otras tres que guardan las temperaturas media, máxima y mínima.

3. ¿Qué unidades se utilizan para la temperatura?
Las tres temperaturas (media, máxima y mínima) vienen en grados Celsius (°C). Lo vemos en datos["daily_units"].

5. ¿Cuántas fechas y temperaturas has obtenido?
Hemos obtenido 31 fechas y 31 temperaturas medias, una por cada día de enero. Lo he comprobado con len()

8. ¿Qué sucede si intentas acceder a una posición que no existe?
Si intento acceder a una posición que no existe, Python da un error IndexError y el programa para. Por ejemplo, la lista time tiene 31 elementos, con índices del 0 al 30, así que la posición 31 no existe.

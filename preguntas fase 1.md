1. ¿Qué información proporciona el servicio?
El servicio da la temperatura máxima, la mínima y la media de cada día del mes de enero de 2025 en Jaén en Celsius.
2. ¿Qué significan latitude y longitude?
La posición desde donde se mide la temperatura. Latitude dice norte-sur y longitude dice este-oeste.
3. ¿Qué fechas se están consultando?
Se consultan las fechas desde el 1 hasta el 31 de enero de 2025.
4. ¿Qué información solicitan temperature_2m_mean , temperature_2m_max y temperature_2m_min?
temperature_2m_mean = temperatura media a 2 metros del suelo.
temperature_2m_max = temperatura máxima a 2 metros del suelo.
temperature_2m_min = temperatura mínima a 2 metros del suelo.
5. ¿En qué formato se presenta la respuesta?
JSON
6. ¿Qué diferencias observas entre esa respuesta y una lista de Python?
Una lista de Python se escribe entre corchete y aquí está utilizando un diccionario "clave": valor, porque está entre llaves. Dentro de ese diccionario hay listas.
JSON es solo texto. Hasta que Python no lo convierte, no es todavía un diccionario de verdad.
7. ¿Qué ocurriría si cambiásemos end_date para consultar hasta el 15 de enero?
Si cambiamos end_date al 15 de enero, la API devuelve solo 15 días, así que cada lista tiene 15 elementos en vez de 31. Las temperaturas de esos días son las mismas.
8. ¿Qué ventaja tiene consultar una API frente a introducir los datos manualmente?
Consultar una API es más cómodo porque no hay que escribir los datos a mano. Además, hay menos errores, porque los datos llegan directamente sin copiarlos. Y si queremos datos de otra ciudad o de otras fechas, solo hay que cambiar los parámetros del enlace.
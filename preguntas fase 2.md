1. ¿Para qué sirve import requests?
import requests sirve para cargar la biblioteca requests, que nos permite pedir datos a una Página de Internet desde Python. Sin esta línea, Python no sabría qué es requests.get y daría NameError.
2. ¿Qué tipo de objeto es parametros?
Es un diccionario, porque está entre llaves y tiene parejas "clave":valor.
3. ¿Qué diferencia hay entre url y parametros?
url es la dirección de la API ycparámetros son los datos que le pedimos.
4. ¿Qué hacen timeout=30 y raise_for_status()?
timeout=30 quiere decir que si en 30 segundos no te contestan, vuelve y avisa. En español, timeout se puede traducir como tiempo máximo de espera.
raise_for_status() mira si contestó bien o con un error. Si da error, el programa para y avisa del error.
5. ¿Qué diferencia hay entre respuesta y datos?
respuesta es el paquete tal como llega, cerrado, con la información todavía como texto JSON, y datos es lo que hay dentro, ya sacado y ordenado. El paso de uno a otro lo hace la línea datos = respuesta.json(), que convierte el texto JSON en un diccionario de Python.
6. ¿Qué podría ocurrir si falla la conexión o el servidor devuelve un error?
Si el servidor devuelve un error, raise_for_status() para el programa y sale un HTTPError (por ejemplo, 404 si la direción no existe). Si falla la conexión, sale un ConnectionError o, si tarda más de 30 segundos, un Timeout. En los dos casos el programa se para y no conseguimos los datos.
7. ¿Por qué separamos los parámetros de la dirección URL?
Porque es más fácil encontrar qué parámetro queremos cambiar y más difícil de equivocarse.
Y tampoco hace falta poner ? y &, porque requests los pone solo al montar el enlace.
8. ¿En qué se diferencia una petición GET de una petición POST?
Get se usa para pedir datos, para leerlos y post para enviar datos, para que se guarden o se procesen.
Get no cambia nada en el servidor, solo consulta. Post guarda o crea algo.
Get los datos van en el propio enlace, después del ?. Post van dentro del sobre no se ven en el enlace.
en nuestro programa utilizamos Get, porque queremos consultar datos solamente no guardarlos.
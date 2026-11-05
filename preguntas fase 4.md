1. ¿Cuáles son las cinco primeras y las cinco últimas temperaturas?
print(temperaturas[0:5]) --> [7.1, 7.3, 7.4, 8.1, 9.5]
print(temperaturas[-5:]) --> [14.8, 9.1, 8.1, 7.4, 6.6]
2. ¿Cuántos valores contiene la lista?
print(len(temperaturas)) --> 31
3. ¿Cuál es la diferencia entre la temperatura más alta y la más baja?
print("Diferencia entre la temperatura máxima y mínima:", max(temperaturas) - min(temperaturas)) --> 10.5
4. ¿Cuántos días superaron los 15 °C? ¿Cuántos estuvieron por debajo de 10 °C?
print("Días que superaron los 15 grados:", len([t for t in temperaturas if t > 15])) --> 0
print("Días que estuvieron por debajo de 10 grados:", len([t for t in temperaturas if t < 10]))--> 19
5. Crea una lista con las temperaturas superiores a 15 °C y otra con temperaturas inferiores a 10 °C.
superiores_15 = [t for t in temperaturas if t > 15]
inferiores_10 = [t for t in temperaturas if t < 10]

print(superiores_15) --> []
print(inferiores_10) --> [7.1, 7.3, 7.4, 8.1, 9.5, 7.1, 8.3, 6.0, 4.3, 5.2, 5.2, 5.1, 6.0, 6.3, 7.5, 9.1, 8.1, 7.4, 6.6]
6. Comprueba si todas las temperaturas son superiores a 0 °C y si alguna supera los 20 °C.
print(any(t > 20 for t in temperaturas)) --> False
print(all(t > 0 for t in temperaturas)) --> True
7. Redondea los valores a un decimal y guarda el resultado en otra lista.
redondeadas = [round(t) for t in temperaturas]
print("Redondeadas:", redondeadas) --> Redondeadas: [7, 7, 7, 8, 10, 10, 7, 8, 12, 10, 12, 11, 6, 4, 5, 5, 5, 6, 6, 8, 13, 14, 13, 10, 10, 11, 15, 9, 8, 7, 7]
8. Ordena las temperaturas de menor a mayor sin alterar la lista original.
print(sorted(temperaturas)) --> [4.3, 5.1, 5.2, 5.2, 6.0, 6.0, 6.3, 6.6, 7.1, 7.1, 7.3, 7.4, 7.4, 7.5, 8.1, 8.1, 8.3, 9.1, 9.5, 10.2, 10.2, 10.3, 10.4, 10.6, 11.3, 12.0, 12.3, 12.6, 12.8, 14.4, 14.8]
Uso sorted() porque crea una lista nueva ordenada y deja la original sin cambios. En cambio, .sort() ordena la misma lista.
9. Calcula la diferencia entre cada temperatura y la media del periodo. Nos interesa los valores absolutos.
media = sum(temperaturas) / len(temperaturas)
diferencias = [round(t - media, 1) for t in temperaturas]
print("Diferencias con la media:", diferencias)
Diferencias con la media: [-1.7, -1.5, -1.4, -0.7, 0.7, 1.4, -1.7, -0.5, 3.5, 1.5, 3.2, 1.8, -2.8, -4.5, -3.6, -3.6, -3.7, -2.8, -2.5, -1.3, 4.0, 5.6, 3.8, 1.6, 1.4, 2.5, 6.0, 0.3, -0.7, -1.4, -2.2]

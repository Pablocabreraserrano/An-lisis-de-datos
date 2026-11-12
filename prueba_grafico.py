import matplotlib.pyplot as plt

dias = [1, 2, 3]
temps = [7.1, 7.3, 7.4]

plt.plot(dias, temps)
plt.title("Mi primer gráfico")
plt.xlabel("Día")
plt.ylabel("Temperatura (°C)")
plt.savefig("prueba.png")
plt.show()
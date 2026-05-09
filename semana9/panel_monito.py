from datetime import datetime

servicios = ["ssh", "nginx", "fail2ban", "apache"]

server = input("Servidor a revisar: ")
espacio_usado = int(input("Qué porcentaje de disco se encuentra en uso: "))
espacio_total = int(input("Cuál es la capacidad total del disco: "))


def calcular_uso(usado, total):
	return ( usado * 100) / total

porcentaje = calcular_uso(espacio_usado, espacio_total)

if porcentaje >= 80 :
	print("Libere espacio porque el disco está en riesgo de llenarse ")


def log(mensaje):
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
	print(timestamp + mensaje)

for i in servicios:
	log(f"Acabas de llamar al servicio {i}")
	if i == "nginx":
		print("La página se encuentra activa")

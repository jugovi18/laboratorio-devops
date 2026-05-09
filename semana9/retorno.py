def calcular_uso (usado, total):
	return ( usado * 100 ) / total

usado = int(input("Cuanto disco se está utilizando?"))
total = int(input("Cual es la capacidad total del disco?"))
espacio_uso = calcular_uso(usado, total)

print(f"El espacio usado es de {espacio_uso}%")

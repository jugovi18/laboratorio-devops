espacio = int(input("Qué capacidad del disco está utilizado:"))


if espacio > 80:
    print("El disco está saturado")
elif espacio > 60:
    print("El disco está bien")
else:
    print("Todo bien")

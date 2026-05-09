from datetime import datetime

servicio = ["ssh", "nginx", "ufw" ]

def log(mensaje):
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(f"{timestamp} {mensaje} está corriendo" )


for corriendo in servicio:
	log (corriendo)
	if corriendo == "nginx" :
			print ("Arriba esa web")

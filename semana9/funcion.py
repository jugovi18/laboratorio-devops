from datetime import datetime

def log(mensaje):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} | {mensaje}")


log("Sistema iniciado")
log("Disco comprobado")

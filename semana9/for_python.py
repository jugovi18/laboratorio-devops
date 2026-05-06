servicios = ["nginx", "ssh", "ufw"] 
for servicio in servicios: 
       if servicio == "nginx" : 
            print(f"Servicio web activo")
       else:
            print(f"Servicio {servicio} ")

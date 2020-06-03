import requests

def cursos_disponibles():
    """[accede al url de donde extrae la lista de cursos disponibles
         y los se los muestra al usuario]"""
    URL = "http://leoviquez.synology.me/VisionAPI/cursos.py"
    r = requests.get(url = URL)
    results = eval(r.text)
    for x in results:
        print (x)

def listar_emociones(id):
    cont=0
    URL = "http://leoviquez.synology.me/VisionAPI/cursos.py?id={0}".format(id)
    r = requests.get(url = URL)
    results = eval(r.text)
    for x in results:
        c=results[x]
        print(c[1])




        
    

while True:
    a=input("Digite el numero:\n1 ver cursos disponibles\n2 ver listado del registros de emociones de por curso\n3 Ver detalles de registros de emociones\n4 salir del sistema")
    if(a=="1"):
        print(cursos_disponibles())
    elif(a=="2"):
        id=(input("Digite el id del grupo:"))
        while True:
            b=input("Digigite el numero:\n1 Listar registros de emociones\n2 Regresar al menú principal")
            if(b=="1"):
                print(listar_emociones(id))
            elif(b=="2"):
                break
    elif(a=="3"):
        while True:
            b=input("Digite el numero:\n1 Detalle del registro\n2 Estadísticas de reconocimientos\n3 Regresar al menu principal")
            if(b=="1"):
                print("detalle_registro")
            elif(b=="2"):
                print("estadisticas")
            elif(b=="3"):
                break
    elif(a=="4"):
        break



            




                    


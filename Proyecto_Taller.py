import requests
from operator import itemgetter
c=(range(1, 5))
def cursos_disponibles():
    """[accede al url de donde extrae la lista de cursos disponibles
         y los se los muestra al usuario]"""   
    URL = "http://leoviquez.synology.me/VisionAPI/cursos.py"
    r = requests.get(url = URL)
    results = eval(r.text)
    cont=0
    while cont<len(results):
        print("------------------------------------")
        print("Id de grupo:",results[cont][0])
        print("código del curso:",results[cont][1])
        print("nombre:",results[cont][2])
        print("grupo:",results[cont][3])
        print("profesor:",results[cont][4])
        print("semestre:",results[cont][5])
        print("año:",results[cont][6])
        print("------------------------------------")
        cont=cont+1

def listar_emociones(id):
    """[Esta función extrae los registros de emociones
        almacenados en al base de datos]

    Args:
        id ([string]): [esta variable es el identificador del grupo para ingresar al registro de este grupo]
    """
    URL = "http://leoviquez.synology.me/VisionAPI/cursos.py?id={0}".format(id)
    r = requests.get(url = URL)
    results = eval(r.text)
    cont=0
    while cont<len(results):
        print("------------------------------------")
        print("Id de registro:",results[cont][0])
        print("Día:",results[cont][1])
        print("Mes:",results[cont][2])
        print("Año:",results[cont][3])
        print("Hora:",results[cont][4])
        print("Minuto:",results[cont][5])
        print("Segundo:",results[cont][6])
        print("------------------------------------")
        cont=cont+1
            
def detalle_registro(id):
    cont=0
    cont2=0
    cont3=0
    URL = "http://leoviquez.synology.me/VisionAPI/index.py?id={0}".format(id)
    r = requests.get(url = URL)
    results = eval(r.text)
    while cont<
    print("\n{}".format(results[0]["fecha"]))
    print("\n{}".format(results[0]["curso"]))
    print("\n{}".format(results[0]["rostros"]))
      

   
while True:
    a=input("\nElija la opción deseada\n----------------------------\n1 ver cursos disponibles\n2 ver listado del registros de emociones de por curso\n3 Ver detalles de registros de emociones\n4 salir del sistema\n----------------------------\nOpcion:")
    if(a=="1"):
            cursos_disponibles()
    elif(a=="2"):
         id=(input("Digite el id del grupo:"))
         while True:
            b=input("\n----------------------------\nElija la opción deseada\n----------------------------\n1 Listar registros de emociones\n2 Regresar al menú principal\n----------------------------\nOpcion:")
            if(b=="1"):
                listar_emociones(id)
            elif(b=="2"):
                break
            elif(b!=c):
                print("\n*El valor es erróneo, digite un valor correcto*")   
    elif(a=="3"):
        while True:
            b=input("\nElija la opción deseada\n----------------------------\n1 Detalle del registro\n2 Estadísticas de reconocimientos\n3 Regresar al menu principal\n----------------------------\nOpcion:")
            if(b=="1"):
                id=(input("Digite el id de registro:"))
                detalle_registro(id)
            elif(b=="2"):
                print("estadisticas")
            elif(b=="3"):
                break
            elif(b!=c):
                print("\n*El valor es erróneo, digite un valor correcto*")
    elif(a=="4"):
        print("------------------------------------\nGracias por utilizar la aplicaión\n------------------------------------")
        break
    elif(a!=c):
            print("\n*El valor es erróneo, digite un valor correcto*")
        




            




                    


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
        print("#Cursos Disponibles#")
        print("\tId de grupo:",results[cont][0])
        print("\tcódigo del curso:",results[cont][1])
        print("\tnombre:",results[cont][2])
        print("\tgrupo:",results[cont][3])
        print("\tprofesor:",results[cont][4])
        print("\tsemestre:",results[cont][5])
        print("\taño:",results[cont][6])
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
        print("#Registros de emociones por curso#")
        print("\tId de registro:",results[cont][0])
        print("\tDía:",results[cont][1])
        print("\tMes:",results[cont][2])
        print("\tAño:",results[cont][3])
        print("\tHora:",results[cont][4])
        print("\tMinuto:",results[cont][5])
        print("\tSegundo:",results[cont][6])
        print("------------------------------------")
        cont=cont+1
            
def detalle_registro(id):
    """[Esta función extrae los detalles de cada registro realizado
        almacenados en al base de datos]

    Args:
        id ([string]): [es un identificador utilizado para ingresar al enlace con los datos deseados ]
    """
    URL = "http://leoviquez.synology.me/VisionAPI/index.py?id={0}".format(id)
    r = requests.get(url = URL)
    results = eval(r.text)
    d=len(results[0]["rostros"])
    print("\n----------------------------")
    print("#Carga de las imagenes#")
    print("\tDía:{}".format(results[0]["fecha"]["dia"]))
    print("\tMes:{}".format(results[0]["fecha"]["mes"]))
    print("\tAño:{}".format(results[0]["fecha"]["a\u00f1o"]))
    print("\tHora:{}".format(results[0]["fecha"]["hora"]))
    print("\tMinuto:{}".format(results[0]["fecha"]["minuto"]))
    print("\tFecha:{}".format(results[0]["fecha"]["segundo"]))
    print("----------------------------")
    print("#Datos del grupo pertenciente#")
    print("\tcodigo del curso:{}".format(results[0]["curso"]["codigo"]))
    print("\tCurso:{}".format(results[0]["curso"]["Curso"]))
    print("\tGrupo:{}".format(results[0]["curso"]["grupo"]))
    print("\tProfesor:{}".format(results[0]["curso"]["profesor"]))
    print("\tSemestre:{}".format(results[0]["curso"]["semestre"]))
    print("\tAño:{}".format(results[0]["curso"]["a\u00f1o"])) 
    print("----------------------------")
    print("#cantidad de rostros cargados#")
    print("\tCantidad:",d)
    print("----------------------------")

def estadisticas(id):
    URL = "http://leoviquez.synology.me/VisionAPI/index.py?id={0}".format(id)
    valor=0
    valor1=0
    valor2=0
    valor3=0
    valor4=0
    r = requests.get(url = URL)
    results = eval(r.text)
    d=len(results[0]["rostros"])
    conteo=(results[0]["rostros"][0]["face_expressions"]["joy_likelihood"])
    if conteo=="VERY_LIKELY":
        valor=(5/d)*20
    if conteo=="LIKELY":
        valor1=(4/d)*20
    if conteo=="POSSIBLE":
        valor2=(3/d)*20
    if conteo=="UNLIKELY":
        valor3=(2/d)*20
    if conteo=="VERY_UNLIKELY":
        valor4=1    
    print(valor,valor1,valor2,valor3,valor4)

while True:
    a=input("\nElija la opción deseada\n----------------------------\n1 ver cursos disponibles\n2 ver listado del registros de emociones por curso\n3 Ver detalles de registros de emociones\n4 salir del sistema\n----------------------------\nOpcion:")
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
    elif(a=="3"):#Aqui intente utilizarlo per me da error 
        while True:
            b=input("\nElija la opción deseada\n----------------------------\n1 Detalle del registro\n2 Estadísticas de reconocimientos\n3 Regresar al menu principal\n----------------------------\nOpcion:")
            if(b=="1"):
                    try:
                        id=(input("----------------------------\nDigite el id de registro:"))  
                        detalle_registro(id)
                    except TypeError as error:
                        print("*El id es erroneo*")                       
            elif(b=="2"):
                id=(input("----------------------------\nDigite el id de registro:"))
                estadisticas(id)
            elif(b=="3"):
                break
            elif(b!=c):
                print("\n*El valor es erróneo, digite un valor correcto*")
    elif(a=="4"):
        print("------------------------------------\nGracias por utilizar la aplicaión\n------------------------------------")
        break
    elif(a!=c):
            print("\n*El valor es erróneo, digite un valor correcto*")
        




            




                    


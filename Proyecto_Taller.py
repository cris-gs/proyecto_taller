import requests
from operator import itemgetter
c=(range(1, 5))   
URL = "http://leoviquez.synology.me/VisionAPI/cursos.py"
r = requests.get(url = URL)
results = eval(r.text)
###################################################################
def menor(results):
    """[Esta función obtiene el id menor]

    Args:
        results ([type:list]): [Esta lista obtiene los datos que se encuentran en la base de datos del enlace] 

    return(Esta retor en valor a tupla_menor que es un dato de tipo tupla, así al retornar cambia el valor de la tupla_menor)
    """
    tupla_menor=results[0]
    for e in results[1:]:
        if tupla_menor[0]>e[0]:
            tupla_menor=e
    return(tupla_menor)
###################################################################
def ordenar(results):
    """[Esta función ordena los valores de menores que los va obteniendo en la
     tupla_menor de la funciion menor  que es una lista a la y los agrega lm de forma ordenada]

    Args:
        results ([type:list]): [Esta lista obtiene los datos que se encuentran en la base de datos del enlace]
    return(retorna el valor de lm )
    """
    lm=[]
    while len(results)>0:
        tupla_menor=menor(results)
        lm.append(tupla_menor)
        results.remove(tupla_menor)
    return(lm)
###################################################################
def cursos_disponibles(results):
    """[Esta funcion imprime identificando cada dato que se presenta en la lista results, esta
    es ordenada por medio de la funcion ordenar que es llamada antes de imprimir los datos]

    Args:
        results ([type:list]): [Esta lista obtiene los datos que se encuentran en la base de datos del enlace]
    """
    cont=0
    results=ordenar(results)
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
###################################################################
def listar_emociones(id):
    """[Esta función extrae los registros de emociones
        almacenados en al base de datos, y los impreme de forma ordenada según su fecha más reciente]

    Args:
        id ([type:str]): [Esta variable es el identificador del grupo para ingresar
         al registro de este grupo]
    """
    URL = "http://leoviquez.synology.me/VisionAPI/cursos.py?id={0}".format(id)
    r = requests.get(url = URL)
    results1 = eval(r.text)
    cont=0
    if (results1==[]):
        print("\n*El id está fuera rango, regrese al menu principal*")#evita que el programa se caiga si que el identificador es invalido
    else:
        #convierte las tuplas que se encuentran en results1 a listas dentro de una la lista results3 
        d=len(results1)
        results3=[]
        for i in range(0,d):
            i=int(i)
            results2=list(results1[i])
            results3.append(results2)
        pasadas=len(results3)-1
        while pasadas>0:
            pos=0
            while pos<pasadas:
                #ordena sun dia, mes y año las listas dentro de la lista results3 
                if results3[pos][1:4]<results3[pos+1][1:4]:
                    temp=results3[pos][1:4]
                    results3[pos][1:4]=results3[pos+1][1:4]
                    results3[pos+1][1:4]=temp
                pos=pos+1
            pasadas=pasadas-1
        cont=0
        while cont<len(results1):
                #imprime estiquetando los datos de las listas dentro de results3
                print("------------------------------------")
                print("#Registros de emociones por curso#")
                print("\tId de registro:",results3[cont][0])
                print("\tDía:",results3[cont][1])
                print("\tMes:",results3[cont][2])
                print("\tAño:",results3[cont][3])
                print("\tHora:",results3[cont][4])
                print("\tMinuto:",results3[cont][5])
                print("\tSegundo:",results3[cont][6])
                print("------------------------------------")
                cont=cont+1
###################################################################            
def detalle_registro(id):
    """[Esta función extrae los detalles de cada registro de imagenes realizado según el id
        que se ha almacenado en al base de datos, e imprime etiquetando los datos de cada registro]

    Args:
        id ([type:str]): [Es un identificador utilizado para ingresar al enlace con los datos deseados ]
    """
    URL = "http://leoviquez.synology.me/VisionAPI/index.py?id={0}".format(id)
    r = requests.get(url = URL)
    results = eval(r.text)
    if (results==[]):
        print("\n*El id está fuera rango*")
    else:
        d=len(results[0]["rostros"])
        print("\n----------------------------")
        print("#Carga de las imagenes#")
        print("\tDía: {}".format(results[0]["fecha"]["dia"]))
        print("\tMes: {}".format(results[0]["fecha"]["mes"]))
        print("\tAño: {}".format(results[0]["fecha"]["a\u00f1o"]))
        print("\tHora: {}".format(results[0]["fecha"]["hora"]))
        print("\tMinuto: {}".format(results[0]["fecha"]["minuto"]))
        print("\tFecha: {}".format(results[0]["fecha"]["segundo"]))
        print("----------------------------")
        print("#Datos del grupo pertenciente#")
        print("\tcodigo del curso: {}".format(results[0]["curso"]["codigo"]))
        print("\tCurso: {}".format(results[0]["curso"]["Curso"]))
        print("\tGrupo: {}".format(results[0]["curso"]["grupo"]))
        print("\tProfesor: {}".format(results[0]["curso"]["profesor"]))
        print("\tSemestre: {}".format(results[0]["curso"]["semestre"]))
        print("\tAño: {}".format(results[0]["curso"]["a\u00f1o"])) 
        print("----------------------------")
        print("#cantidad de rostros cargados#")
        print("\tCantidad:",d)
        print("----------------------------")
###################################################################
def estadisticas(id):
    """[Esta funcion extrae los datos de las imagenes registradas
     según el identificador en la base de datos, e imprime la estadistica de las 
     emociones encontradas por la appi de google]

    Args:
        id ([type:str]): [Es un identificador utilizado para ingresar al enlace con los datos deseados]
    """
    URL = "http://leoviquez.synology.me/VisionAPI/index.py?id={0}".format(id)
    r = requests.get(url = URL)
    results = eval(r.text)
    if (results==[]):
        print("\n*El id está fuera rango*")
    else:
        d=len(results[0]["rostros"])
        cont=0
        cont1=0
        cont2=0
        cont3=0
        cont4=0
        cont5=0
        cont6=0
        valor=0
        valor1=0
        valor2=0
        valor3=0
        valor4=0
        while cont<d:
            #realiza un acumulador del puntaje por la emoción definida
            conteo=(results[0]["rostros"][cont]["face_expressions"]["joy_likelihood"])
            if conteo=="VERY_LIKELY":
                valor=valor+5
            elif conteo=="LIKELY":
                valor1=valor1+4
            elif conteo=="POSSIBLE":
                valor2=valor2+3
            elif conteo=="UNLIKELY":
                valor3=valor3+2
            elif conteo=="VERY_UNLIKELY":
                valor4=valor4+1
            cont=cont+1
        #imprime el valor del acumulador dividido entre la cantidad de imagenes y multiplicado por 20
        print("----------------------------\nLa probabilidad de alegria es:#")
        print("\tMuy probable: {}%".format((valor/d)*20))
        print("\tProbable: {}%".format((valor1/d)*20))
        print("\tPosible: {}%".format((valor2/d)*20))
        print("\tImprobable: {}%".format((valor3/d)*20))
        print("\tMuy improbable: {}%".format((valor4/d)*20))
        valor=0
        valor1=0
        valor2=0
        valor3=0
        valor4=0
        while cont1<d:
            conteo=(results[0]["rostros"][cont1]["face_expressions"]["sorrow_likelihood"])
            if conteo=="VERY_LIKELY":
                valor=valor+5
            elif conteo=="LIKELY":
                valor1=valor1+4
            elif conteo=="POSSIBLE":
                valor2=valor2+3
            elif conteo=="UNLIKELY":
                valor3=valor3+2
            elif conteo=="VERY_UNLIKELY":
                valor4=valor4+1
            cont1=cont1+1
        print("----------------------------\n#La probabilidad de tristeza es:#")
        print("\tMuy probable: {}%".format((valor/d)*20))
        print("\tProbable: {}%".format((valor1/d)*20))
        print("\tPosible: {}%".format((valor2/d)*20))
        print("\tImprobable: {}%".format((valor3/d)*20))
        print("\tMuy improbable: {}%".format((valor4/d)*20))
        valor=0
        valor1=0
        valor2=0
        valor3=0
        valor4=0
        while cont2<d:
            conteo=(results[0]["rostros"][cont2]["face_expressions"]["anger_likelihood"])
            if conteo=="VERY_LIKELY":
                valor=valor+5
            elif conteo=="LIKELY":
                valor1=valor1+4
            elif conteo=="POSSIBLE":
                valor2=valor2+3
            elif conteo=="UNLIKELY":
                valor3=valor3+2
            elif conteo=="VERY_UNLIKELY":
                valor4=valor4+1
            cont2=cont2+1
        print("----------------------------\n#La probabilidad de ira es:#")
        print("\tMuy probable: {}%".format((valor/d)*20))
        print("\tProbable: {}%".format((valor1/d)*20))
        print("\tPosible: {}%".format((valor2/d)*20))
        print("\tImprobable: {}%".format((valor3/d)*20))
        print("\tMuy improbable: {}%".format((valor4/d)*20))
        valor=0
        valor1=0
        valor2=0
        valor3=0
        valor4=0
        while cont3<d:
            conteo=(results[0]["rostros"][cont3]["face_expressions"]["surprise_likelihood"])
            if conteo=="VERY_LIKELY":
                valor=valor+5
            elif conteo=="LIKELY":
                valor1=valor1+4
            elif conteo=="POSSIBLE":
                valor2=valor2+3
            elif conteo=="UNLIKELY":
                valor3=valor3+2
            elif conteo=="VERY_UNLIKELY":
                valor4=valor4+1
            cont3=cont3+1
        print("----------------------------\n#La probabilidad de sorpresa es:#")
        print("\tMuy probable: {}%".format((valor/d)*20))
        print("\tProbable: {}%".format((valor1/d)*20))
        print("\tPosible: {}%".format((valor2/d)*20))
        print("\tImprobable: {}%".format((valor3/d)*20))
        print("\tMuy improbable: {}%".format((valor4/d)*20))
        valor=0
        valor1=0
        valor2=0
        valor3=0
        valor4=0
        while cont4<d:
            conteo=(results[0]["rostros"][cont4]["face_expressions"]["under_exposed_likelihood"])
            if conteo=="VERY_LIKELY":
                valor=valor+5
            elif conteo=="LIKELY":
                valor1=valor1+4
            elif conteo=="POSSIBLE":
                valor2=valor2+3
            elif conteo=="UNLIKELY":
                valor3=valor3+2
            elif conteo=="VERY_UNLIKELY":
                valor4=valor4+1
            cont4=cont4+1
        print("----------------------------\n#La probabilidad subexpuesta es:#")
        print("\tMuy probable: {}%".format((valor/d)*20))
        print("\tProbable: {}%".format((valor1/d)*20))
        print("\tPosible: {}%".format((valor2/d)*20))
        print("\tImprobable: {}%".format((valor3/d)*20))
        print("\tMuy improbable: {}%".format((valor4/d)*20))
        valor=0
        valor1=0
        valor2=0
        valor3=0
        valor4=0
        while cont5<d:
            conteo=(results[0]["rostros"][cont5]["face_expressions"]["blurred_likelihood"])
            if conteo=="VERY_LIKELY":
                valor=valor+5
            elif conteo=="LIKELY":
                valor1=valor1+4
            elif conteo=="POSSIBLE":
                valor2=valor2+3
            elif conteo=="UNLIKELY":
                valor3=valor3+2
            elif conteo=="VERY_UNLIKELY":
                valor4=valor4+1
            cont5=cont5+1
        print("----------------------------\n#La probabilidad borrosa es:#")
        print("\tMuy probable: {}%".format((valor/d)*20))
        print("\tProbable: {}%".format((valor1/d)*20))
        print("\tPosible: {}%".format((valor2/d)*20))
        print("\tImprobable: {}%".format((valor3/d)*20))
        print("\tMuy improbable: {}%".format((valor4/d)*20))
        valor=0
        valor1=0
        valor2=0
        valor3=0
        valor4=0
        while cont6<d:
            conteo=(results[0]["rostros"][cont6]["face_expressions"]["headwear_likelihood"])
            if conteo=="VERY_LIKELY":
                valor=valor+5
            elif conteo=="LIKELY":
                valor1=valor1+4
            elif conteo=="POSSIBLE":
                valor2=valor2+3
            elif conteo=="UNLIKELY":
                valor3=valor3+2
            elif conteo=="VERY_UNLIKELY":
                valor4=valor4+1
            cont6=cont6+1
        print("----------------------------\n#La probabilidad de sombreros es:#")
        print("\tMuy probable: {}%".format((valor/d)*20))
        print("\tProbable: {}%".format((valor1/d)*20))
        print("\tPosible: {}%".format((valor2/d)*20))
        print("\tImprobable: {}%".format((valor3/d)*20))
        print("\tMuy improbable: {}%".format((valor4/d)*20))
        print("----------------------------")
###################################################################
while True:
    """[Este es el menu de opciones quien hace 
    los llamados a las funciones según la opción elegida por el usuario ]
    """
    a=(input("\nElija la opción deseada\n----------------------------\n1 ver cursos disponibles\n2 ver listado del registros de emociones por curso\n3 Ver detalles de registros de emociones\n4 salir del sistema\n----------------------------\nOpcion:"))
    if(a=="1"):#opcion uno del menu
        cursos_disponibles(results)
    elif(a=="2"):#opcion dos del menu
        try:
            id=int((input("Digite el id del grupo:")))
        except ValueError as error:
            print("\n*El id es erroneo, vuelva a ingresar*")
            break
        while True:
            b=input("\n----------------------------\nElija la opción deseada\n----------------------------\n1 Listar registros de emociones\n2 Regresar al menú principal\n----------------------------\nOpcion:")
            if(b=="1"):#opcion uno del submenu
                listar_emociones(id)
            elif(b=="2"):#opcion dos del submenu
                break
            elif(b!=c):
                print("\n*El valor es erróneo, digite un valor correcto*")   
    elif(a=="3"):#opcion tres del menu
        while True:
            b=input("\nElija la opción deseada\n----------------------------\n1 Detalle del registro\n2 Estadísticas de reconocimientos\n3 Regresar al menu principal\n----------------------------\nOpcion:")
            if(b=="1"):#opcion uno del submenu
                    try:
                        id=int((input("----------------------------\nDigite el id de registro:"))) 
                        detalle_registro(id)
                    except ValueError as error:
                        print("*El id es erroneo*")                       
            elif(b=="2"):#opcion dos del submenu
                try:
                    id=int((input("----------------------------\nDigite el id de registro:")))
                    estadisticas(id)
                except ValueError as error:
                    print("*El id es erroneo*")
            elif(b=="3"):#opcion tres del submenu
                break
            elif(b!=c):
                print("\n*El valor es erróneo, digite un valor correcto*")
    elif(a=="4"):#opcion cuatro del menu
        print("------------------------------------\nGracias por utilizar la aplicaión\n------------------------------------")
        break
    elif(a!=c):#Evita que el string que digita el usuario este fuera de las opciones del menu
            print("\n*El valor es erróneo, digite un valor correcto*")
        




            




                    


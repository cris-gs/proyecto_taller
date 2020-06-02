while True:
        a=input("Digite el numero:\n1 ver cursos disponibles\n2 ver listado del registros de emociones de por curso\n3 Ver detalles de registros de emociones\n4 salir del sistema")
        if(a=="1"):
            print("cursos_disponibles")
        elif(a=="2"):
            while True:
                b=input("Digigite el numero:\n1 Listar registros de emociones\n2 Regresar al menú principal")
                if(b=="1"):
                    print("listar_emociones")
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

        



            




                    


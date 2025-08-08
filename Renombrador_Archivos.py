import os, traceback,shutil

#Asignar la ruta a usar en el script Manualmente, de manera raw o cruda, para evitar la deteccion de comandos
ruta = r'C:\Users\David\Documents\Aprender_Python\Mini_Proyectos_1\Renombrador_de_Archivos'
#Variables Auxiliares:
nuevaRuta=""
opcion=0
validar = False
while opcion == 0:
    try:
        opcion = input("\n Ejecucion del programa mediante : 1 - Ruta Manual  2 - Introducir Ruta  3 - Exit: ")
        if opcion == "1":
            #Ejecuta el programa con la informacion que tenga la variable "ruta"

            #Comprobar si la ruta es valida
            validarRuta = os.path.exists(ruta)
        elif opcion == "2":
            #Ejecuta el progrma con un ruta pasada por el usuario en caso de no saber como mannejar codigo
            nuevaRuta = os.path.join(nuevaRuta,input("\n\n Introduzca la ruta donde se encuenta el Script: "))
            validarRuta = os.path.exists(nuevaRuta)
        elif opcion == "3":
            break
        else:
            print("*** La opcion escogida es No es correcta, Intentelo Nuevamente ***")
        
        if opcion == "1" or opcion == "2" :
            if validarRuta == False :
                print("\n*** La Ruta no es valida, Vuelve a intentarlo ***") 
            else:   
                #Validar si la ruta es realmente la ruta donde se encuentra el Script
                if os.path.exists(os.path.join(nuevaRuta,"Archivos_Originales")) == False :
                    print("\n*** Esta No es la Ruta donde se encuentra el Script, Introduzca la Ruta del Script ***")       
                elif os.path.exists(os.path.join(ruta,"Archivos_Originales")) == False:     
                    print("\n*** Esta No es la Ruta donde se encuentra el Script, Introduzca la Ruta del Script ***")
                else:
                   validar = True
                   if opcion == "2":
                       ruta = nuevaRuta
                    
        #El programa solo puede avanzar si la ruta es la del Script
        if validar == False:
            opcion = 0
            nuevaRuta = ""

    except:
        raise Exception("*** Error escogiendo la opcion ***") 


if opcion == "3":
    print("\n\n Saliste del Programa...")
else:
    try:
        #Carpetas a usar
        entrada = os.path.join(ruta,"Archivos_Originales")
        salida = os.path.join(ruta,"Archivos_Renombrados")
        #Con esto cambiamos la ruta en la que el script se ejecutara o la carpeta en la que buscara los archivos a renombrar
        os.chdir(entrada)
        #Imprimir el contenido de esa ruta, archivos, carpetas, etc...
        archivos = os.listdir() 
        print("\n Archivos en la Carpeta : \n\n",archivos)

        opcion=0
        #Ordenar los archivos por Nombre o Fecha
        while opcion ==0:
            try:
                opcion = input("\n Selecciona el tipo de Ordenamiento : 1 - Nombre  2 - Fecha  3 - Exit:")
                if opcion == "1":
                    #Ordenar por Nombre
                    archivos.sort(key = os.path.dirname)
                elif opcion == "2":
                    #Ordenar por Fecha
                    archivos.sort(key = os.path.getctime)
                elif opcion == "3":
                    break
                else:
                    print("*** La opcion escogida es No es correcta, Intentelo Nuevamente ***")
                    opcion=0
            except:
                raise Exception("*** Error escogiendo la opcion ***")    
        
        if opcion == "3":
            print("\n\n Saliste del Progama...")
        else:
            #variable auxiliar que sirve de contador para la impresion de Cliente 1,2,3,etc...
            i=0
            #Se plantea la base del renombre de archivos y el tipo de archivo / extension
            formatoBase = "Cliente_"
            tipoArchivo = ".pdf"
            #Creacion de la carpeta donde se copiaron los archivos de ser necesario
            if os.path.exists(salida) == False:
                os.makedirs(salida)

            #Recorre la ruta, recibiendo en la variable archivo el nombre sus elementos
            for archivo in archivos:
                #Comprobamos si el elemento actual es un archivo o no para avanzar a la siguiente evaluacion, ya que solo interesa trabajar con archivos
                if os.path.isfile(archivo):
                    #Comprobamos si el archivo es del tipo que se pide ya que es unico formato que se usara en el script
                    if archivo.endswith(tipoArchivo):
                        #Se copian los archivos y se les cambia el nombre
                        shutil.copy(archivo, os.path.join(salida, (formatoBase + str((i+1)) + tipoArchivo)))
                        i+=1
            #Muestra el resultado final de los elementos en la ruta
            print("\n Archivos Renombados y Ordenados : \n\n ", os.listdir(salida),"\n\n Proceso Finalizado...")

    except:
        #Imprimir mensaje en caso de que la ruta este mal escrita o no exista
        if FileNotFoundError:
            raise Exception("Revise si la ruta asignada es la correcta")



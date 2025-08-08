import os, traceback,shutil

#Acceder a la ruta del Script (La misma que el ejecutable)
ruta =os.getcwd()

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
            opcion = input("\n Selecciona el tipo de Ordenamiento : 1 - Nombre  2 - Fecha  3 - Exit: ")
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

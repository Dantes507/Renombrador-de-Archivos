import os, traceback,shutil

#Acceder a la ruta del Script (La misma que el ejecutable)
ruta =os.getcwd()

try:
    #Carpetas a usar
    entrada = os.path.join(ruta,"Archivos_Originales")
    salida = os.path.join(ruta,"Archivos_Organizados")
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
        #Diccionario con los tipos de extension a manejar
        tipoArchivo = {".pdf": "PDF",".docx": "WORD",".xlsx": "Excel",".csv": "CSV",".jpg": "JPG",".png": "PNG"}
        #Creacion de la carpeta donde se copiaron los archivos de ser necesario
        if os.path.exists(salida) == False:
            os.makedirs(salida)

        #Recorre la ruta, recibiendo en la variable archivo el nombre sus elementos
        for archivo in archivos:
            #Comprobamos si el elemento actual es un archivo o no para avanzar a la siguiente evaluacion, ya que solo interesa trabajar con archivos
            if os.path.isfile(archivo):           
                #Recorrido de los tipos de extensiones a comparar
                for tipo in tipoArchivo.keys():
                   #Comprueba si el archivo es de un tipo que maneja en el script
                    if  archivo.endswith(tipo):
                        #Obtiene la ruta de la carpeta donde se guardaria el archivo segun el tipo de extension
                        carpetaTipo = os.path.join(salida,tipoArchivo[tipo])
                        #Si la carpeta no existe la crea
                        if os.path.exists(carpetaTipo) == False:
                            os.makedirs(carpetaTipo)
                        #Se mueve el archivo a su respectiva carpeta
                        if os.path.exists(os.path.join(carpetaTipo,archivo)):
                            print("\n El archivo ", archivo, " Existe dentro de la carpeta ", tipoArchivo[tipo], " se omitira...")
                            continue
                        else:
                            shutil.move(archivo, os.path.join(carpetaTipo,archivo))
        
        #Muestra el contenido de las carpetas segun las extensiones
        for nombreCarpeta, subCarpeta, nombreArchivo in os.walk(salida):
            #Muesta el nombre de la carpeta actual
            carpeta = os.path.basename(nombreCarpeta)
            #Imprime el archivo de esa carpeta
            print("\n",carpeta,": ",str(nombreArchivo))
        print("\n\n Proceso Finalizado...")

except:
    #Imprimir mensaje en caso de que la ruta este mal escrita o no exista
    if FileNotFoundError:
        raise Exception("Revise si la ruta asignada es la correcta")

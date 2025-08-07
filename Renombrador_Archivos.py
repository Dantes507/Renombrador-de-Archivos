import os, traceback,shutil

#Asignar la ruta a usar en el script
ruta = "C:\\Users\\David\\Documents\\Aprender_Python\\Mini_Proyectos_1\\Renombrador_de_Archivos"

try:
    #Carpetas a usar
    entrada = "Archivos_Originales"
    salida = "Archivos_Renombrados"
    #Con esto cambiamos la ruta en la que el script se ejecutara o la carpeta en la que buscara los archivos a renombrar
    os.chdir(os.path.join(ruta,entrada))
    #Imprimir el contenido de esa ruta, archivos, carpetas, etc...
    print(os.listdir())
    #variable auxiliar que sirve de contador para la impresion de Cliente 1,2,3,etc...
    i=0
    #Se plantea la base del renombre de archivos y el tipo de archivo / extension
    formatoBase = "Cliente_"
    tipoArchivo = ".pdf"
    #Se especifica la ruta de salida de los archivos renombrados
    ruta = os.path.join(ruta,salida)

    #Recorre la ruta, recibiendo en la variable archivo el nombre sus elementos
    for archivo in os.listdir():
        #Comprobamos si el elemento actual es un archivo o no para avanzar a la siguiente evaluacion, ya que solo interesa trabajar con archivos
        if os.path.isfile(archivo):
            #Comprobamos si el archivo es del tipo que se pedia ya que es unico formato que se usara en el script
            if archivo.endswith(tipoArchivo):
                #Se copian los archivos y se les cambia el nombre
                shutil.copy(archivo, os.path.join(ruta, (formatoBase + str((i+1)) + tipoArchivo)))

                i+=1
except:
        #Imprimir mensaje en caso de que la ruta este mal escrita o no exista
        if FileNotFoundError:
           raise Exception("Revise si la ruta asignada es la correcta")

#Muestra el resultado final de los elementos en la ruta
print(os.listdir(ruta))

#Organizador de Archivos


#Este script de Python mueve los archivos a diferentes carpetas según la extensión de cada uno. Se puede utilizar para documentos,
pdf, Excel, png, jpg, csv, etc...


#Funcionamiento

1. Lee los archivos de la subcarpeta "Archivos_Originales".
2. Ordena los archivos por Nombre o Fecha.
3. Discrimina los archivos por su tipo de extensión.
4. Crea las subcarpetas según el tipo de extensión de los archivos, dentro de la carpeta "Archivos_Organizados".
5. Mueve los archivos a estas subcarpetas según su extensión (si hay algún archivo duplicado omite el proceso para ese archivo).


#Requisitos

- Python 3
- Liberias : os, traceback y shutil (vendrían incluidas con Python)
-Si las librerías no vienen instaladas seguir los siguientes pasos:

1. Abrir el CMD
2. Introduce la ruta donde instalaste Python -> usando: cd + "Ruta especifica"
3. Ingresa pip + "Nombre de la librería" y se descargara e instalara.


#Guia de Uso

1. Colocas los archivos que quieres renombrar en la subcarpeta "Archivos_Originales".
2. Doble Click sobre el ejecutable ("Organizador_Archivos_Ejecutable").
3. Seleccionas la opción de Ordenamiento de los archivos (Nombre o Fecha).
4. Se ejecuta el ordenamiento, mueve los archivos a sus diferentes subcarpetas dentro de "Archivos_Organizados".
5. Proceso Terminado.


Extra : 

 El Proyecto viene con unos archivos para ser probado.


#Actualizaciones Posibles

- Identificar varios tipos de extensiones a la vez, renombrarlos y/o guardarlos en subcarpetas especificas.
- Implementar interfaz amigable con el usuario


#Autor

Proyecto Realizado como Practica de Automatización para crecer como programador 

David Ortega

Versión 1.0.0

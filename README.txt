#Renombrador de Archivos


#Este script de Python renombra automáticamente todos los archivos dentro de una carpeta
y los copia a otra aplicando un formato simple que se puede utilizar para documentos,
pdf, excel o imágenes, etc...


#Funcionamiento

1. Lee los archivos de la subcarpeta "Archivos_Originales".
2. Ordena los archivos por Nombre o Fecha.
3. Discrimina por el tipo de extensión que se le pide
4. Renombra los archivos con el formato simple indicado
5. Guarda los archivos copiados y renombrados en la subcarpeta "Archivos_Renombrados". 


#Requisitos

- Python 3
- Liberias : os, traceback y shutil (vendrían incluidas con Python)
-Si las librerías no vienen instaladas seguir los siguientes pasos:

1. Abrir el CMD
2. Introduce la ruta donde instalaste Python -> usando: cd + "Ruta especifica"
3. Ingresa pip + "Nombre de la librería" y se descargara e instalara.


#Guia de Uso

1. Colocas los archivos que quieres renombrar en la subcarpeta "Archivos_Originales".
2. Doble Click sobre el ejecutable ("Renombrador_Archivos_Ejecutable").
3. Seleccionas la opción de Ordenamiento de los archivos (Nombre o Fecha).
4. Se ejecuta el ordenamiento, renombra los archivos y los copia en la subcarpeta "Archivos_Renombrados".
5. Proceso Terminado.


Extra : 

1. El Proyecto viene con unos archivos para ser probado.
2. El formato de renombre puede ser modificado en el código igual que el tipo de extensión.



#Actualizaciones Posibles

- Identificar varios tipos de extensiones a la vez, renombrarlos y/o guardarlos en subcarpetas especificas.
- Implementar interfaz amigable con el usuario


#Autor

Proyecto Realizado como Practica de Automatización para crecer como programador 

David Ortega

Versión 1.2.1

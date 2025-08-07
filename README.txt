#Renombrador de Archivos


#Este script de Python renombra automáticamente todos los archivos dentro de una carpeta
y los copia a otra aplicando un formato simple que se puede utilizar para documentos,
pdf, excel o imágenes


#Funcionamiento

1. Lee los archivos de la subcarpeta "Archivos_Originales".
2. Discrimina por el tipo de extensión que se le pide
3. Renombra los archivos con el formato simple indicado
4. Guarda los archivos copiados y renombrados en la subcarpeta "Archivos_Renombrados". 


#Requisitos

- Python 3
- Liberias : os, traceback y shutil (vendrían incluidas con Python)
-Si las librerías no vienen instaladas seguir los siguientes pasos:

1. Abrir el CMD
2. Introduce la ruta donde instalaste Python -> usando: cd + "Ruta especifica"
3. Ingresa pip + "Nombre de la librería" y se descargara e instalara.


#Guia de Uso

1. Colocas los archivos que quieres renombrar en la subcarpeta "Archivos_Originales".
2. Colocas la ruta donde esta el programa de ejecución del script en la variable "ruta".
3. (Opcional)Cambias el Formato de renombre que tiene de base "Cliente_" en la variable "formato_Base" y/o
cambias el tipo de extensión que deseas usar(pdf, png, docs, etc...).
4. Ejecutas el script y ya tienes tus archivos renombrados, ordenados y copiados en la subcarpeta "Archivos_Renombrados". 

Extra : El Proyecto viene con unos archivos para ser probado.



#Actualizaciones Posibles

- Identificar varios tipos de extensiones a la vez, renombrarlos y guardarlos en subcarpetas especificas.
- Implementar interfaz amigable con el usuario


#Autor

Proyecto Realizado como Practica de Automatización para crecer como programador 

David Ortega


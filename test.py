import subprocess

def ejecutarComandoDesdeArchivo(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
    for i, linea in enumerate(lineas):
        print(f'Procesando {linea}')
        #Construir el comando seguido de la ruta y ejecutar en termianl
        #comando = f'youtube-dl --geo-bypass -f bestvideo+bestaudio -o "./descargas/%(title)s.%(ext)s" "{linea}"'
        #subprocess.run(comando, shell=True)
        
        #Elimina la línea actual del archivo
        with open(archivo, 'w') as f:
            f.writelines(lineas[i + 1:])            
        #Actualiza la lista de líneas para reflejar el cambio en el archivo
        lineas = lineas[i + 1:]
        
rutaArchivo = 'URLsADescargar.txt'
ejecutarComandoDesdeArchivo(rutaArchivo)

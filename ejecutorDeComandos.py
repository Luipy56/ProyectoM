import subprocess

def ejecutarComandoDesdeArchivo(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            #Construir el comando seguido de la ruta
            comando = f'youtube-dl --geo-bypass -f bestvideo+bestaudio -o "./descargas/%(title)s.%(ext)s" "{linea}"'

            #Ejecutar el comando en la terminal
            subprocess.run(comando, shell=True)

            # Eliminar la línea del archivo
            with open(archivo, 'w') as f:
                for line in lines:
                    if line.strip() != linea.strip():
                        f.write(line)
rutaArchivo = 'test.txt'
ejecutarComandoDesdeArchivo(rutaArchivo)

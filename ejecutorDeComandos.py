import subprocess

RESET = "\033[0m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
VERDE = "\033[32m"
def printAmarillo(texto):
    print(f"{YELLOW}{texto}{RESET}")
def printBlue(texto):
    print(f"{BLUE}{texto}{RESET}")
def printRojo(texto):
    print(f"{RED}{texto}{RESET}")
def printVerde(texto):
    print(f"{VERDE}{texto}{RESET}")

def ejecutarComandoDesdeArchivo(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            #Construir el comando seguido de la ruta
            comando = f'youtube-dl --geo-bypass -f bestvideo-bestaudio -o "RUTAAAAAA" "{linea}"'

            #Ejecutar el comando en la terminal
            subprocess.run(comando, shell=True)

            # Eliminar la línea del archivo
            with open(archivo, 'r') as f:
                lines = f.readlines()
            with open(archivo, 'w') as f:
                for line in lines:
                    if line.strip() != linea.strip():
                        f.write(line)
rutaArchivo = 'test.txt'
ejecutarComandoDesdeArchivo(rutaArchivo)

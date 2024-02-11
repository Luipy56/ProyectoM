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
            comando = f'dir "{linea}"'

            #Ejecutar el comando en la terminal
            subprocess.run(comando, shell=True)

rutaArchivo = 'test.txt'
ejecutarComandoDesdeArchivo(rutaArchivo)
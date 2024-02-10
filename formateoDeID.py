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

def procesarLinea(linea):
    #Sacar ID según tipo de link y formatearla
    printAmarillo(f"Procesando línea: {linea}")
    if linea[13]==".":
        printBlue("Es un share normal")
        lineaProcesada=pieDeURL+linea[17:28]
    elif linea[8]=="y":
        printBlue("Es un share short")
        lineaProcesada=pieDeURL+linea[27:38]
    elif linea[24]=="w":
        printBlue("Es una URL normal")
        lineaProcesada=linea
    elif linea[24]=="s":
        printBlue("Es una URL short")
        lineaProcesada=pieDeURL+linea[31:42]
    else: printBlue("Something wrong")
    
    return lineaProcesada

def procesarArchivo(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r') as archivo_lectura:
            with open(archivo_salida, 'w') as archivo_escritura:
                for linea in archivo_lectura:
                    #Comprobar si es un URL limpia (empieza por h)
                    if linea.startswith('h'):
                        printVerde("Es un URL")
                    else:
                        printRojo("No es un URL puro, formateando a URL...")
                        #Buscar la primera aparición de "h" en el string y
                        #hacer substring a partir de la h
                        linea=linea[linea.find('h'):]
                            
                    lineaProcesada=procesarLinea(linea.strip())
                    
                    #Buscar en archivo 2 si la ID ya existe
                    if buscar_frase_en_archivo(lineaProcesada, archivo_a_verificar):
                        printRojo(f"La frase '{lineaProcesada}' SÍ está en el archivo almacén.")
                    else:
                        printVerde(f"La frase '{lineaProcesada}' NO está en el archivo.")
                        #Escribe la línea en el archivo de salida.
                        archivo_escritura.write(lineaProcesada.rstrip() + '\n')

        printAmarillo("Proceso completado.")
    except FileNotFoundError:
        printAmarillo(f"Error: No se pudo encontrar el archivo {archivo_entrada}.")
    except Exception as e:
        printRojo(f"Error inesperado: {str(e)}")

def buscar_frase_en_archivo(frase, ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if frase in linea:
                    return True  # La frase está en el archivo
            return False  # La frase no está en el archivo
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no fue encontrado.")
        return False
    except Exception as e:
        print(f"Error inesperado: {e}")
        return False
    
#Nombre del archivo de entrada y salida
archivo_entrada = 'ProyectoM/URLsNuevas.txt'
archivo_salida = 'ProyectoM/URLsADescargar.txt'
archivo_a_verificar = "ProyectoM/AlmacenURLs.txt"
pieDeURL="https://www.youtube.com/watch?v="

#Llama a la función para procesar el archivo
procesarArchivo(archivo_entrada, archivo_salida)


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
                    
                    #Procesar linea para sacar ID
                    lineaProcesada=procesarLinea(linea.strip())
                    
                    #Buscar en archivo 2 si la ID en la linea ya existe
                    if buscarLineaEnAlmacen(lineaProcesada, archivoAlmacen):
                        printRojo(f"La frase '{lineaProcesada}' SÍ está en el archivo almacén.")
                    else:
                        printVerde(f"La frase '{lineaProcesada}' NO está en el archivo.")
                        #Escribe la línea en el archivo de salida.
                        archivo_escritura.write(lineaProcesada.rstrip() + '\n')
                    printBlue("Siguiente línea")

        printAmarillo("Proceso completado.")
    except FileNotFoundError:
        printAmarillo(f"Error: No se pudo encontrar el archivo {archivo_entrada}.")
    except Exception as e:
        printRojo(f"Error inesperado: {str(e)}")

def buscarLineaEnAlmacen(frase, ruta_archivo):
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

def verificarLineasRepetidas(archivo):
    try:
        with open(archivo, 'r') as file:
            lineas = file.readlines()
            
            # Eliminar caracteres de nueva línea al final de cada línea
            lineas = [linea.strip() for linea in lineas]

            # Verificar si hay líneas duplicadas
            if len(lineas) == len(set(lineas)):
                print("No hay líneas duplicadas en el archivo.")
            else:
                print("Se encontraron líneas duplicadas en el archivo.")
                lineas_duplicadas = set()
                lineas_repetidas = [linea for linea in lineas if linea in lineas_duplicadas or lineas_duplicadas.add(linea)]
                print("Líneas duplicadas:")
                for linea in lineas_repetidas:
                    print(linea)
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
def almacenarLineas(archivo2,archivo3):
    with open(archivo2, 'r') as f2, open(archivo3, 'a') as f3:
        lineas = f2.readlines()
        f3.writelines(lineas)

#Variables
archivoNuevas = 'URLsNuevas.txt'
archivoProcesado = 'URLsADescargar.txt'
archivoAlmacen = "AlmacenURLs.txt"
pieDeURL="https://www.youtube.com/watch?v="

#Llama a la función para procesar el archivo
procesarArchivo(archivoNuevas, archivoProcesado)
#Llamar función lineas repetidas
verificarLineasRepetidas(archivoProcesado)
#Llamar función almacenado
almacenarLineas(archivoProcesado, archivoAlmacen)


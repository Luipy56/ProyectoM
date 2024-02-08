def procesarLinea(linea):
    #Formateo de ID
    print("Procesando línea:", linea)
    if linea[13]==".":
        print("Es un share normal")
        lineaProcesada=pieDeURL+linea[17:28]
    elif linea[8]=="y":
        print("Es un share short")
        lineaProcesada=pieDeURL+linea[27:38]
    elif linea[24]=="w":
        print("Es una URL normal")
        lineaProcesada=linea
    elif linea[24]=="s":
        print("Es una URL short")
        lineaProcesada=pieDeURL+linea[31:42]
    else: print("Something wrong")
    
    if buscar_frase_en_archivo(lineaProcesada, archivo_a_verificar):
        print(f"La frase '{lineaProcesada}' está en el archivo.")
    else:
        print(f"La frase '{lineaProcesada}' no está en el archivo.")
    
    return lineaProcesada

def procesarArchivo(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r') as archivo_lectura:
            with open(archivo_salida, 'w') as archivo_escritura:
                for linea in archivo_lectura:
                    #Llama a la función X con cada línea leída.
                    lineaProcesada=procesarLinea(linea.strip())
                    #Escribe la línea en el archivo de salida.
                    archivo_escritura.write(lineaProcesada.rstrip() + '\n')
        print("Proceso completado.")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {archivo_entrada}.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

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
archivo_entrada = 'ProyectoM/archivo1.txt'
archivo_salida = 'ProyectoM/archivo2.txt'
archivo_a_verificar = "ProyectoM/archivo3.txt"

pieDeURL="https://www.youtube.com/watch?v="





#Llama a la función para procesar el archivo
procesarArchivo(archivo_entrada, archivo_salida)


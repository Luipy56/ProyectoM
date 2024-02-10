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

# Ejemplo de uso
frase_a_buscar = "https://www.youtube.com/watch?v=CD58TWGIcsQ"
archivo_a_verificar = "ProyectoM/archivo2.txt"

if buscar_frase_en_archivo(frase_a_buscar, archivo_a_verificar):
    print(f"La frase '{frase_a_buscar}' está en el archivo.")
else:
    print(f"La frase '{frase_a_buscar}' no está en el archivo.")

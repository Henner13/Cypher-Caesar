# Caesar Cypher de archivos.txt

# Función para cifrar un texto con el desplazamiento que el usuario elija (evitar 1, 3 o 13)
def cifrar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():  # Si es una letra (no espacios ni signos)
            base = ord('A') if letra.isupper() else ord('a')  # Detecta si es mayúscula o minúscula
            # Calcula la nueva letra desplazada
            resultado += chr((ord(letra) - base + desplazamiento) % 26 + base)
        else:
            resultado += letra  # Si no es letra, se deja igual
    return resultado

# Para descifrar, simplemente se invierte el desplazamiento
def descifrar(texto, desplazamiento):
    return cifrar(texto, -desplazamiento)

# Función para leer el contenido de un archivo de texto
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print("Error: El archivo no existe.")
        return None
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return None

# Menú principal del programa
while True:
    print("\n--- MENÚ CIFRADO CÉSAR ---")
    print("1. Cifrar mensaje desde archivo")
    print("2. Descifrar mensaje desde archivo")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        archivo = input("Nombre del archivo a cifrar (ej: mensaje.txt): ")
        texto = leer_archivo(archivo)
        if texto:
            try:
                desplazamiento = int(input("Introduce el desplazamiento: "))
                print("Mensaje cifrado:\n", cifrar(texto, desplazamiento))
            except ValueError:
                print("Error: El desplazamiento debe ser un número entero.")

    elif opcion == "2":
        archivo = input("Nombre del archivo a descifrar (ej: mensaje.txt): ")
        texto = leer_archivo(archivo)
        if texto:
            try:
                desplazamiento = int(input("Introduce el desplazamiento usado para cifrar: "))
                print("Mensaje descifrado:\n", descifrar(texto, desplazamiento))
            except ValueError:
                print("Error: El desplazamiento debe ser un número entero.")

    elif opcion == "3":
        print("¡Chao, pescao !")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")

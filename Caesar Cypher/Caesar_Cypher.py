# Cypher Caesar

def cifrar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            resultado += chr((ord(letra) - base + desplazamiento) % 26 + base)
        else:
            resultado += letra
    return resultado

def descifrar(texto, desplazamiento):
    return cifrar(texto, -desplazamiento)

# Menú principal
while True:
    print("\n--- MENÚ CIFRADO CÉSAR ---")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        mensaje = input("Introduce el mensaje a cifrar: ")
        desplazamiento = int(input("Introduce el desplazamiento: "))
        print("Mensaje cifrado:", cifrar(mensaje, desplazamiento))

    elif opcion == "2":
        mensaje = input("Introduce el mensaje a descifrar: ")
        desplazamiento = int(input("Introduce el desplazamiento usado para cifrar: "))
        print("Mensaje descifrado:", descifrar(mensaje, desplazamiento))

    elif opcion == "3":
        print("¡Chao, pescao!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")

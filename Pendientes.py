# Programa para registrar pendientes

# Lista para almacenar los pendientes
pendientes = []

def mostrar_menu():
    print("\nGestor de Pendientes")
    print("1. Agregar pendiente")
    print("2. Ver pendientes")
    print("3. Marcar pendiente como completado")
    print("4. Salir")

def agregar_pendiente():
    pendiente = input("Escribe el pendiente que quieres agregar: ")
    pendientes.append({"tarea": pendiente, "completado": False})
    print(f"Pendiente '{pendiente}' agregado con éxito.")

def ver_pendientes():
    if not pendientes:
        print("No hay pendientes registrados.")
    else:
        print("\nLista de Pendientes:")
        for i, pendiente in enumerate(pendientes, start=1):
            estado = "✔" if pendiente["completado"] else "✘"
            print(f"{i}. {pendiente['tarea']} [{estado}]")

def completar_pendiente():
    ver_pendientes()
    if pendientes:
        try:
            numero = int(input("Introduce el número del pendiente que completaste: "))
            if 1 <= numero <= len(pendientes):
                pendientes[numero - 1]["completado"] = True
                print(f"Pendiente '{pendientes[numero - 1]['tarea']}' marcado como completado.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_pendiente()
        elif opcion == "2":
            ver_pendientes()
        elif opcion == "3":
            completar_pendiente()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()

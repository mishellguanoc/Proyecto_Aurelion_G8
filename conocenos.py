from utils.presentador import limpiar, escribir, mostrar_titulo, mostrar_lista, cargar_info
import time

def bienvenida(info):
    limpiar()
    escribir("✨ Bienvenido al Proyecto Aurelion ✨", 0.04)
    time.sleep(0.4)
    escribir("\nNos alegra tenerte aquí. Somos el Grupo #8 de la Camada #12.", 0.03)
    escribir("Este proyecto nació del deseo de ayudar al señor Raúl, dueño de un supermercado local,", 0.03)
    escribir("a comprender mejor su negocio mediante los datos.", 0.03)
    escribir("\n¿Quieres saber más sobre nuestro trabajo? 🚀", 0.03)
    input("\nPresiona ENTER para continuar...")

def mostrar_menu(info):
    opciones = {
        "1": "Tema del proyecto",
        "2": "Problemática",
        "3": "Solución propuesta",
        "4": "Dataset y estructura de datos",
        "5": "Proceso y pasos realizados",
        "6": "Equipo Aurelion",
        "0": "Salir"
    }

    while True:
        limpiar()
        mostrar_titulo("MENÚ PRINCIPAL")
        mostrar_lista(list(opciones.values())[:-1])
        print("\n0. Salir\n")
        eleccion = input("Selecciona una opción: ")

        if eleccion == "1":
            limpiar()
            mostrar_titulo("TEMA")
            print(info["tema"])
        elif eleccion == "2":
            limpiar()
            mostrar_titulo("PROBLEMÁTICA")
            print(info["problema"])
        elif eleccion == "3":
            limpiar()
            mostrar_titulo("SOLUCIÓN PROPUESTA")
            print(info["solucion"])
        elif eleccion == "4":
            limpiar()
            mostrar_titulo("DATASET Y ESTRUCTURA")
            print(f"Fuente: {info['dataset']['fuente']}")
            print(f"Objetivo: {info['dataset']['objetivo']}\n")
            print("Tablas incluidas:")
            mostrar_lista(info["dataset"]["tablas"])
        elif eleccion == "5":
            limpiar()
            mostrar_titulo("PROCESO DE ANÁLISIS")
            print("Pasos principales realizados:\n")
            mostrar_lista(info["proceso"])
        elif eleccion == "6":
            limpiar()
            mostrar_titulo("EQUIPO AURELION")
            print(f"Camada: {info['grupo']['camada']}")
            print("Integrantes:")
            mostrar_lista(info["grupo"]["integrantes"])
        elif eleccion == "0":
            despedida()
            break
        else:
            print("Opción no válida, intenta nuevamente.")
        
        input("\nPresiona ENTER para volver al menú...")

def despedida():
    limpiar()
    escribir("\nGracias por conocer nuestro proyecto, esperamos que te haya inspirado 🌙", 0.04)
    escribir("Equipo Aurelion — Camada 12.", 0.04)
    time.sleep(0.8)

def main():
    info = cargar_info()
    bienvenida(info)
    mostrar_menu(info)

if __name__ == "__main__":
    main()

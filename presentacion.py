import os
import time

# UTILS

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def escribir(texto, velocidad=0.03):
    """Imprime texto con efecto máquina de escribir (solo para bienvenida/despedida)."""
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(velocidad)
    print()

def mostrar_titulo(titulo):
    print("\n" + "=" * len(titulo))
    print(titulo.upper())
    print("=" * len(titulo))

def mostrar_lista(items):
    for i, item in enumerate(items, start=1):
        print(f"  {i}. {item}")

# INFO DEL PROYECTO

info = {
    "grupo": {
        "nombre": "Aurelion",
        "camada": "12",
        "integrantes": [
            "Mishell Guano",
            "Laura Becerra",
            "Cristhian Mallorquin",
            "Emanuel Acosta",
            "Natalia Garzón",
            "Nicolás Buitrago",
            "Stevhen Quispe"
        ]
    },
    "tema": "Análisis exploratorio y visual de los datos relacionales de ventas de un supermercado.",
    "problema": (
        "El dueño de un supermercado registra la información de su comercio en cuatro tablas relacionadas: "
        "productos, clientes, ventas y detalle_ventas. Conforme el negocio crece, la interpretación manual se vuelve lenta, "
        "dificultando obtener métricas clave para tomar decisiones estratégicas."
    ),
    "solucion": (
        "Desarrollar un programa en Python que integre, analice y visualice los datos del supermercado. "
        "La herramienta permitirá identificar productos más vendidos, clientes destacados, tendencias de ventas "
        "y categorías más rentables, transformando registros en información útil."
    ),
    "dataset": {
        "fuente": "Archivos Excel transformados a CSV: clientes, ventas, detalle_ventas, productos.",
        "objetivo": "Transformar datos brutos en información comprensible para detectar patrones y oportunidades.",
        "tablas": ["Clientes", "Productos", "Ventas", "Detalle_ventas"]
    },
    "proceso": [
        "Conversión de archivos Excel a CSV.",
        "Lectura y validación de datos.",
        "Preprocesamiento: limpieza, tipos de datos, duplicados y normalización.",
        "EDA: análisis exploratorio de relaciones entre variables.",
        "Identificación de métricas clave y generación de gráficos.",
        "Interpretación de resultados y creación de dashboard interactivo.",
        "Exportación de reportes finales en PDF, Power BI o Notebook."
    ]
}

# Presentacion interactiva

def bienvenida():
    limpiar()
    escribir("✨ Bienvenido al Proyecto Aurelion ✨", 0.04)
    time.sleep(0.4)
    escribir("\nNos alegra tenerte aquí. Somos el Grupo #8 de la Camada #12.", 0.03)
    escribir("Este proyecto nació del deseo de ayudar al señor Raúl, dueño de un supermercado local,", 0.03)
    escribir("a comprender mejor su negocio mediante los datos.", 0.03)
    escribir("\n¿Quieres saber más sobre nuestro trabajo? 🚀", 0.03)
    input("\nPresiona ENTER para continuar...")

def mostrar_menu():
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



if __name__ == "__main__":
    bienvenida()
    mostrar_menu()

import time
import os
import json

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def escribir(texto, velocidad=0.03):
    """Imprime texto con efecto máquina de escribir."""
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(velocidad)
    print()

def mostrar_titulo(titulo):
    print("\n" + "="*len(titulo))
    print(titulo.upper())
    print("="*len(titulo))

def mostrar_lista(items):
    for i, item in enumerate(items, start=1):
        print(f"  {i}. {item}")

def cargar_info():
    ruta = os.path.join("data", "info_proyecto.json")
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

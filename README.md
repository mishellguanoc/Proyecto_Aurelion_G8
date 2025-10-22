# Proyecto Aurelion

## Descripción General

Este proyecto es una aplicación interactiva en Python que presenta información sobre el Proyecto Aurelion, desarrollado por el Grupo #8 de la Camada #12, desarrollado dentro de la formacion de GUAYERD y con el respaldo de IBM SkillsBuild. El objetivo es mostrar, de manera amigable, el propósito, problemática, solución y equipo detrás del proyecto, utilizando datos cargados desde un archivo JSON.

---

## Estructura de Archivos

- `conocenos.py`: Script principal que gestiona la interacción con el usuario y la navegación por el menú.
- `utils/presentador.py`: Módulo de utilidades para la presentación visual y carga de datos.
- `data/info_proyecto.json`: Archivo con la información del proyecto (tema, problemática, solución, dataset, proceso, equipo).

---

## Descripción de Funciones

### conocenos.py

- **bienvenida(info)**
  - Limpia la pantalla y muestra un mensaje de bienvenida con animación tipo máquina de escribir.
  - Presenta el objetivo del proyecto y solicita al usuario continuar.

- **mostrar_menu(info)**
  - Muestra un menú principal con opciones para conocer distintos aspectos del proyecto.
  - Permite navegar entre tema, problemática, solución, dataset, proceso y equipo.
  - Utiliza funciones de presentación para mostrar títulos y listas.
  - Permite salir del programa.

- **despedida()**
  - Muestra un mensaje de despedida animado.

- **main()**
  - Carga la información del proyecto desde el archivo JSON.
  - Llama a la función de bienvenida y luego al menú principal.

---

### utils/presentador.py

- **limpiar()**
  - Limpia la consola, compatible con Windows y Unix.

- **escribir(texto, velocidad=0.03)**
  - Imprime texto con efecto de máquina de escribir, controlando la velocidad de aparición de los caracteres.

- **mostrar_titulo(titulo)**
  - Muestra un título centrado y subrayado.

- **mostrar_lista(items)**
  - Muestra una lista numerada de elementos.

- **cargar_info()**
  - Carga y retorna la información del proyecto desde `data/info_proyecto.json`.

---

## Ejecución

Para ejecutar el programa principal:

```bash
python conocenos.py
```

---

# 1° Entrega - Proyecto Aurelion  
**Grupo #8 - Camada #12**

---

## Desarrollo de la documentación

### Tema, Problema y Solución

#### Tema
**Análisis exploratorio y visual de los datos relacionales de ventas de un supermercado.**

#### Problema
El dueño de un supermercado registra la información de su comercio en cuatro tablas relacionadas: productos, clientes, ventas y detalle de ventas.  
La interpretación manual de los registros se torna más lenta y complicada conforme el negocio crece y la cantidad de transacciones aumenta, incluso si actualmente la cantidad de datos es pequeña (de 100 a 120 registros por tabla).  
Este obstáculo dificulta la obtención rápida de información clave, como los productos más vendidos, las categorías más rentables o los clientes más destacados, lo que limita la capacidad del propietario para tomar decisiones estratégicas basadas en datos.

#### Solución
Crear un **programa en Python** que integre, examine y presente visualmente la información proveniente de las tablas relacionales del supermercado (clientes, productos, ventas y detalle_ventas).  
La herramienta entregará un resumen automatizado del comportamiento del negocio, convirtiendo datos en indicadores claros y gráficos comprensibles.

**Métricas a mostrar**
- Productos más vendidos y volúmenes de venta.  
- Clientes con mayor frecuencia o monto de compra.  
- Promedio mensual de ventas e identificación de tendencias.  
- Categorías más rentables (ej. alimentos, limpieza).  
- Distribución total de productos vendidos por tipo o periodo.

**Beneficio:** Permitir decisiones basadas en datos, identificar oportunidades de mejora, productos más vendidos y patrones de compra.

---

## Referencia Dataset  
**Fuente, definición, estructura, tipos y escala.**

### Clientes
- **Fuente:** Archivo Excel – Hoja `clientes`  
- **Definición:** Información de clientes registrados (datos personales, ciudad y fecha de alta).  
- **Estructura:** Filas: 100 — Columnas: 5  
- **Identificador:** PK: `id_cliente`

| Campo         | Tipo            | Escala de medición | Descripción                              |
|---------------|-----------------|--------------------|-------------------------------------------|
| id_cliente    | Numérico (int)  | Razón              | Identificador único de cliente            |
| nombre_cliente| Texto (string)  | Nominal            | Nombre del cliente                        |
| email         | Texto (string)  | Nominal            | Correo electrónico del cliente            |
| ciudad        | Texto (string)  | Nominal            | Ciudad de residencia                      |
| fecha_alta    | Numérico (datetime) | Intervalo      | Fecha en que se registró el cliente       |

---

### Productos
- **Fuente:** Archivo Excel – Hoja `productos`  
- **Definición:** Catálogo de productos por categoría con precio unitario.  
- **Estructura:** Filas: 100 — Columnas: 4  
- **Identificador:** PK: `id_producto`

| Campo           | Tipo           | Escala de medición | Descripción                         |
|------------------|----------------|--------------------|-------------------------------------|
| id_producto      | Numérico (int) | Razón              | Identificador único del producto    |
| nombre_producto  | Texto (string) | Nominal            | Nombre comercial del producto       |
| categoría        | Texto (string) | Nominal            | Tipo o categoría del producto       |
| precio_unitario  | Numérico (int) | Razón              | Precio de venta por unidad          |

---

### Ventas
- **Fuente:** Archivo Excel – Hoja `ventas`  
- **Definición:** Registro de ventas realizadas por clientes (fecha y medio de pago).  
- **Estructura:** Filas: 120 — Columnas: 6  
- **Identificadores:** PK: `id_venta` — FK: `id_cliente → clientes.id_cliente`

| Campo         | Tipo              | Escala de medición | Descripción                                 |
|---------------|-------------------|--------------------|----------------------------------------------|
| id_venta      | Numérico (int)    | Razón              | Identificador único de la venta (PK)         |
| fecha         | Numérico (datetime)| Intervalo         | Fecha de realización de la venta             |
| id_cliente    | Numérico (int)    | Razón              | Relación con cliente (FK)                    |
| nombre_cliente| Texto (string)    | Nominal            | Nombre del cliente (campo redundante)        |
| email         | Texto (string)    | Nominal            | Email del cliente                            |
| medio_pago    | Texto (string)    | Nominal            | Método de pago utilizado                     |

---

### Detalle_ventas
- **Fuente:** Archivo Excel – Hoja `detalle_ventas`  
- **Definición:** Detalle de cada línea de producto en una venta (producto, cantidad, importe).  
- **Estructura:** Filas: 343 — Columnas: 6  
- **Identificadores:** FK: `id_venta → ventas.id_venta`, FK: `id_producto → productos.id_producto`

| Campo           | Tipo              | Escala de medición | Descripción                                   |
|------------------|-------------------|--------------------|-----------------------------------------------|
| id_venta         | Numérico (int)    | Razón              | Identificador de la venta (FK)                |
| id_producto      | Numérico (int)    | Razón              | Identificador del producto (FK)               |
| nombre_producto  | Texto (string)    | Nominal            | Nombre del producto                           |
| cantidad         | Numérico (int)    | Razón              | Cantidad vendida de ese producto              |
| precio_unitario  | Numérico (int)    | Razón              | Precio por unidad en el momento de la venta   |
| importe          | Fórmula/Numérico  | Razón              | Total por línea: cantidad × precio_unitario   |

---

## Información general del proceso y pasos a seguir

**Objetivo:** Transformar los datos brutos de ventas, clientes y productos en información útil y visualmente comprensible para la toma de decisiones (identificar productos rentables, conocer clientes y visualizar tendencias).

### Pasos
1. **Conversión de formato:** `.xlsx` → `.csv` (Clientes, Ventas, Detalle_ventas, Productos).  
2. **Lectura de datos:** Cargar los archivos `.csv` descritos.  
3. **Preprocesamiento de datos:**  
   - Visualización previa (número de registros y columnas).  
   - Verificación y corrección de tipos de datos.  
   - Detección y tratamiento de valores nulos.  
   - Detección y eliminación/gestión de duplicados.  
   - Normalización/estandarización según corresponda.  
4. **EDA (Análisis Exploratorio de Datos):**  
   - Relacionar variables para determinar:  
     - Clientes destacados (variables: `id_cliente`, `nombre_cliente`, `email`, `ciudad`, `fecha_alta`).  
     - Tendencias mensuales (variables: `id_venta`, `fecha`, `medio_pago`, `precio_unitario`, `cantidad`).  
     - Productos más vendidos (variables: `id_producto`, `nombre_producto`, `importe`, `id_venta`, `fecha`).  
   - Generar gráficas a partir de estas relaciones.  
5. **Identificación de información clave:** Generar indicadores sobre clientes, ventas y productos.  
6. **Análisis e interpretación de resultados:** Resumen automático explicando lo que las métricas, gráficas y correlaciones dicen del negocio.  
7. **Generación de reportes:** Centralizar y exportar información procesada en formatos visuales/tabulares.  
8. **Creación de dashboard interactivo:** Integrar visualizaciones en un tablero con filtros por fecha, ciudad y categoría.  
9. **Exportación de reportes:** Guardar resultados en PDF, Power BI, Notebook Python u otros formatos requeridos.

---

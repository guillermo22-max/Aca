# Venta de entradas a un espectáculo

Programa de consola en Python que calcula cuánto se paga por las entradas a un espectáculo. Se pueden comprar como máximo **4 entradas**, y el descuento depende de la cantidad:

| Entradas | Descuento |
|:--------:|:---------:|
| 1        | 0 %       |
| 2        | 10 %      |
| 3        | 15 %      |
| 4        | 20 %      |

Es un ejercicio de programación orientada a objetos que usa **clases, métodos, constructores**, el **ciclo mientras** (`while`) y el **ciclo para** (`for`).

## Requisitos

- [uv](https://docs.astral.sh/uv/), el gestor de proyectos y paquetes de Python.
- Python 3.12 o superior. Si no lo tienes, uv lo instala.

No hace falta ninguna dependencia externa: el programa solo usa la biblioteca estándar.

## Instalación

```bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>
uv sync
```

`uv sync` crea el entorno virtual (`.venv`) y deja el proyecto listo.

## Ejecución

```bash
uv run main.py
```

## Uso

1. Escribe el precio de una entrada (por ejemplo, `10`).
2. El programa muestra una tabla con lo que costarían de 1 a 4 entradas.
3. Elige cuántas entradas quieres comprar (de 1 a 4).
4. Se muestra la factura con el subtotal, el descuento y el total.
5. Responde `s` para hacer otra compra o `n` para salir.

### Ejemplo

```text
Ingrese el precio de una entrada: 10

Tabla de precios:
  1 entrada(s): 10.00
  2 entrada(s): 18.00
  3 entrada(s): 25.50
  4 entrada(s): 32.00
¿Cuántas entradas desea comprar? (1 a 4): 3

------- FACTURA -------
Precio por entrada: 10.00
Cantidad:           3
Subtotal:           30.00
Descuento (15%):    4.50
TOTAL A PAGAR:      25.50
-----------------------

¿Desea realizar otra compra? (s/n): n
Gracias por su compra.
```

## Estructura del código

### Clase `CompraEntradas`

| Elemento | Descripción |
|----------|-------------|
| `MAX_ENTRADAS` | Constante con el máximo de entradas por compra (4). |
| `__init__(precio_entrada: float, cantidad: int)` | **Constructor**: guarda el precio de una entrada y la cantidad. |
| `obtener_porcentaje_descuento()` | Devuelve el descuento (0.10, 0.15 o 0.20) según la cantidad. |
| `calcular_subtotal()` | Suma el precio de cada entrada con un **ciclo para**. |
| `calcular_descuento()` | Calcula el importe del descuento. |
| `calcular_total()` | Subtotal menos descuento. |
| `mostrar_factura()` | Muestra el detalle de la compra. |
| `mostrar_tabla(precio_entrada)` | Método estático: muestra los precios de 1 a 4 entradas con un **ciclo para**. |

### Funciones

| Función | Descripción |
|---------|-------------|
| `leer_precio()` | Pide el precio con un **ciclo mientras** hasta que sea un número mayor que 0. |
| `leer_cantidad()` | Pide la cantidad con un **ciclo mientras** hasta que esté entre 1 y 4. |
| `main()` | Repite las compras con un **ciclo mientras** mientras el usuario responda `s`. |

## Validaciones

- Si el precio no es un número o es menor o igual a 0, se vuelve a pedir.
- Si la cantidad no es un número entero o está fuera del rango 1–4, se vuelve a pedir.

## Autor

Luis Guillermo Soto Siciliano
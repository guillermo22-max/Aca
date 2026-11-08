# Pago de entradas a un espectáculo (máximo 4 entradas)
# 2 entradas -> 10% | 3 entradas -> 15% | 4 entradas -> 20%

# Clase
class CompraEntradas():
    # Constante
    MAX_ENTRADAS = 4

    # Constructor int
    def __init__(self, precio_entradas: float, cantidad:int):
        self.precio_entradas = precio_entradas
        self.cantidad = cantidad

    # Método: porcentaje de descuento según la cantidad
    def obtener_porcentaje_descuento(self):
        if self.cantidad == 2:
            return 0.10
        elif self.cantidad == 3:
            return 0.15
        elif self.cantidad == 4:
            return 0.20
        return 0.0

    """ Método: subtotal usando el ciclo
        suma el precio de todas las entradas
    """

    def calcular_subtotal(self):
        subtotal = 0.0
        for _ in range(self.cantidad):
            subtotal += self.precio_entradas
        return subtotal

    def calcular_descuento(self):
        return self.calcular_subtotal() * self.obtener_porcentaje_descuento()

    def calcular_total(self):
        return self.calcular_subtotal() - self.calcular_descuento()

    def mostrar_factura(self):
        print("\n------- FACTURA -------")
        print(f"Precio por entrada: {self.precio_entradas:.2f}")
        print(f"Cantidad:           {self.cantidad}")
        print(f"Subtotal:           {self.calcular_subtotal():.2f}")
        print(f"Descuento ({self.obtener_porcentaje_descuento() * 100:.0f}%):    {self.calcular_descuento():.2f}")
        print(f"TOTAL A PAGAR:      {self.calcular_total():.2f}")
        print("-----------------------\n")

     # Método estático: tabla de precios usando el ciclo PARA
    @staticmethod
    def mostrar_tabla(precio_entrada:float):
        print("\nTabla de precios:")
        for cant in range(1, CompraEntradas.MAX_ENTRADAS + 1):
            compra = CompraEntradas(precio_entrada, cant)
            print(f"  {cant} entrada(s): {compra.calcular_total():.2f}")    


def leer_precio():
    precio = -1.0
    # Ciclo MIENTRAS: valida que el precio sea positivo
    while precio <= 0:
        try:
            precio = float(input("Ingrese el precio de una entrada: "))
            if precio <= 0:
                print("El precio debe ser mayor que 0.")
        except ValueError:
            print("Valor no válido.")
    return precio
 
 
def leer_cantidad():
    cantidad = 0
    # Ciclo MIENTRAS: valida que la cantidad esté entre 1 y 4
    while cantidad < 1 or cantidad > CompraEntradas.MAX_ENTRADAS:
        try:
            cantidad = int(input("¿Cuántas entradas desea comprar? (1 a 4): "))
            if cantidad < 1 or cantidad > CompraEntradas.MAX_ENTRADAS:
                print("Solo se pueden comprar de 1 a 4 entradas.")
        except ValueError:
            print("Valor no válido.")
    return cantidad
 
 
def main():
    continuar = "s"
    # Ciclo MIENTRAS: permite realizar varias compras
    while continuar == "s":
        precio = leer_precio()
        CompraEntradas.mostrar_tabla(precio)
        cantidad = leer_cantidad()
 
        compra = CompraEntradas(precio, cantidad)
        compra.mostrar_factura()
 
        continuar = input("¿Desea realizar otra compra? (s/n): ").strip().lower()
    print("Gracias por su compra.")


if __name__ == "__main__":
    main()
 
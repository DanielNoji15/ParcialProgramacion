
def invertir_array(arr):
    return arr[::-1]

if __name__ == "__main__":
    try:
        cantidad_elementos = int(input("Ingrese la cantidad de elementos del array: "))
        if cantidad_elementos <= 0:
            print("La cantidad de elementos debe ser un número entero positivo.")
        else:
            array_original = []
            print("Ingrese los valores de los elementos:")
            for i in range(cantidad_elementos):
                valor = input(f"Elemento {i + 1}: ")
                array_original.append(valor)

            array_invertido = invertir_array(array_original)

            print("\nArray original:", array_original)
            print("Array invertido:", array_invertido)

    except ValueError:
        print("Por favor, ingresar un número entero válido para la cantidad de elementos.")
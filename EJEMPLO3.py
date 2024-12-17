import numpy as np
import matplotlib.pyplot as plt

def print_menu():
    print("\n=== Calculadora de Matrices ===")
    print("1. Sumar dos matrices")
    print("2. Salir")

def input_matrix(name):
    fila = int(input(f"Ingrese el número de filas de la matriz {name}: "))
    columna = int(input(f"Ingrese el número de columnas de la matriz {name}: "))
    print(f"Ingrese los elementos de la matriz {name} fila por fila, separados por espacios:")
    elements = []
    for i in range(fila):
        row = list(map(float, input(f"Fila {i+1}: ").split()))
        elements.append(row)
    return np.array(elements)

def main():
    while True:
        print_menu()
        choice = input("Elija una opción (1-2): ")

        if choice == '1':
            A = input_matrix('A')
            B = input_matrix('B')
            if A.shape == B.shape:
                print("\nResultado de la suma:")
                print(A + B)
            else:
                print("\nError: Las matrices deben tener las mismas dimensiones.")

        elif choice == '2':
            print("Saliendo de la calculadora de matrices. \u00a1Hasta luego!")
            break
        
        else:
            print("\nOpción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()

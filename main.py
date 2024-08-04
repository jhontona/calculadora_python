def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "No se puede dividir por cero"
    else:
        return num1 / num2

def main():
    while True:
        print("**Calculadora básica**")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            resultado = suma(num1, num2)
            print(f"El resultado de la suma es: {resultado}")

        elif opcion == 2:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            resultado = resta(num1, num2)
            print(f"El resultado de la resta es: {resultado}")

        elif opcion == 3:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            resultado = multiplicacion(num1, num2)
            print(f"El resultado de la multiplicación es: {resultado}")

        elif opcion == 4:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            resultado = division(num1, num2)
            print(f"El resultado de la división es: {resultado}")

        elif opcion == 5:
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

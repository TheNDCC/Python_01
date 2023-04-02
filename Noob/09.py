while True:
    num = int(input("Introduce un número entero: "))

    factorial = 1

    for i in range(1, num+1):
        factorial *= i

    print(f"El factorial de {num} es: {factorial}")

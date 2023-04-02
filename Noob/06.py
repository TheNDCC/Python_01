n = int(input("ingrese un numero: "))
if n % 3 == 0 and n % 5 == 0:
    print(n, "fizzbuzz.")
elif n % 3 == 0:
    print(n, "fizz.")
elif n % 5 == 0:
    print(n, "buzz.")
else:
    print(n)
    n = n
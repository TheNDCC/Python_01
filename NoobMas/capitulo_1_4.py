from capitulo_1_0 import get_random_array

lista = get_random_array()


def Suma(lista):
    laSuma = 0
    for i in lista:
        laSuma = laSuma + i
    return laSuma


Cantidad = len(lista)

print(Suma(lista)/Cantidad)

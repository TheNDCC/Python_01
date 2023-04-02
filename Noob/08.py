def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    return sorted(palabra1) == sorted(palabra2)

cadena1 = input("Ingresa una cadena: ")
cadena2 = input("Ingresa otra cadena: ")

if es_anagrama(cadena1, cadena2):
    print(f"{cadena1} es anagrama de {cadena2}")
else:
    print(f"{cadena1} NO es anagrama de {cadena2}")

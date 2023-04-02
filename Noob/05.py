exe = True
while exe:
    print("escriba cualquier palabra?")
    palabra = input()
    print(len(palabra))
    if palabra == "salir":
        exe = False
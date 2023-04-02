def is_palindrome(word):
    return word == word[::-1]

while True:
    word = input("Escriba una palabra: ")
    if word == "salir":
        break
    if is_palindrome(word):
        print(word, "es un palíndromo")
    else:
        print(word, "no es un palíndromo")    
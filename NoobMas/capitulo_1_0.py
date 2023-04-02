from random import randrange


def get_random_array():
    randomer = randrange(5000, 10001)
    array = []
    for i in range(randomer):
        x = randrange(-50000, 50000)
        array.append(x)
    return array

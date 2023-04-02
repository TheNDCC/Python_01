from capitulo_1_0 import get_random_array


def selection_sort(array):
    for i in range(len(array)):
        min_indx = i
        for j in range(i+1, len(array)):
            if array[min_indx] > array[j]:
                min_indx = j
        array[i], array[min_indx] = array[min_indx], array[i]


lista = get_random_array()
selection_sort(lista)

for i in range(10):
    print(lista[i], end=" ")

print("\n")

for i in range(1, 11):
    print(lista[i*-1], end=" ")

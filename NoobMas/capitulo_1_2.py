from capitulo_1_0 import get_random_array


def bubbleSort(array):

    # loop through each element of array
    for i in range(len(array)):

        # keep track of swapping
        swapped = False

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping occurs if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                swapped = True

        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break


lista = get_random_array()
bubbleSort(lista)

for i in range(10):
    print(lista[i], end=" ")

print("\n")

for i in range(1, 11):
    print(lista[i*-1], end=" ")

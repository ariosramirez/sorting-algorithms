# buscarl el numero menor en mi array
# crear dos subarrays para llevar el control de mi algoritmo
# imprimir el resultado del ordenamiento


def selection_sort(array):
    for i in range(len(array)):

        idx_des = i

        for j in range(i + 1, len(array)):
            if array[idx_des] > array[j]:
                idx_des = j
        print(f"index of minimum value: {idx_des}, value: {array[idx_des]}")
        print(array)
        array[i], array[idx_des] = array[idx_des], array[i]


input_array = [3, 124, 412, 13, 235, 2, 323, 3, 212, 1, 25, 5, 3, 323, 6, 3]

selection_sort(input_array)

print("The array sorted ascended: ")
print(input_array)

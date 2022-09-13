# bubble_sort.py
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        swap = False
        for j in range(0, n - i - 1):
            print(array)
            if array[j] > array[j + 1]:
                print(
                    f"swap in progress, values: {array[j + 1]}, {array[j]} are swapping"
                )
                swap = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swap:
            break


input_array = [190, 1200, 1, 2, 4, 55, 100, 6, 800]
bubble_sort(input_array)

print("The array sorted ascended: ")
print(input_array)

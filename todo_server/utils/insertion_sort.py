def insertion_sort(array):
    for i in range(1, len(array)):
        element = array[i]
        j = i-1
        while j >= 0 and element < array[j] :
                array[j + 1] = array[j]
                j -= 1
        arr[j + 1] = key
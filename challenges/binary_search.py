def binary_search(arr, el):
    counter = 0
    for i in arr:
        counter += 1
        if i == el:
            return counter - 1
    return -1



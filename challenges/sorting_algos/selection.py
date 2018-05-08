def selection_sort(lst):
    """
    Selection sort algorithm
    """
    lst = list(lst)
    for i in range(len(lst) - 1):
        min_index = i
        min_val = lst[i]
        j = i + 1
        while j < len(lst):
            if min_val > lst[j]:
                min_index = j
                min_val = lst[j]
            j += 1
        if min_index != i:
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp
    return lst

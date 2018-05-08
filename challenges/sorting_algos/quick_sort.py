def quick_sort(lst):
    less_than = []
    greater_than = []
    equal = []

    lst = list(lst)
    if len(lst) > 1:
        temp = lst[0]
        for i in lst:
            if i < temp:
                less_than.append(i)
            elif i > temp:
                greater_than.append(i)
            else:
                equal.append(i)
        return lst
    else:
        return lst
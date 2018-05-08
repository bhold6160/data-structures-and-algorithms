# def quick_sort(lst):
#     less_than = []
#     greater_than = []
#     equal = []

#     lst = list(lst)
#     if len(lst) > 1:
#         temp = lst[0]
#         for i in lst:
#             if i < temp:
#                 less_than.append(i)
#             if i == temp:
#                 equal.append(i)
#             if i > temp:
#                 greater_than.append(i)
#         return quick_sort(less_than) + equal + quick_sort(greater_than)
#     else:
#         return lst


def quick_sort(lst):
    if not lst:
        return []

    less_than = quick_sort([i for i in lst if i < lst[0]])
    greater_than = quick_sort([i for i in lst if i > lst[0]])
    equal = [i for i in lst if i == lst[0]]

    return less_than + equal + greater_than

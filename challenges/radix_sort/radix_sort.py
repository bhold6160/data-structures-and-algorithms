def radix_sort(lst):
    BASE = 10
    max_len = False
    current_val = -1
    val = 1

    while not max_len:
        max_len = True
        buckets = [[] for _ in range(BASE)]

    for i in lst:
        current_val = i // val
        buckets[current_val % BASE].append(i)
        if max_len and current_val > 0:
            max_len = False

    counter = 0
    for current in range(BASE):
        bucket = buckets[current]
        for item in bucket:
            lst[counter] = item
            counter += 1

    val *= BASE
    return lst


# def radix_sort(aList):
#     RADIX = 10
#     maxLength = False
#     tmp, placement = -1, 1

#     while not maxLength:
#         maxLength = True
#         # declare and initialize buckets
#         buckets = [list() for _ in range(RADIX)]

#     # split aList between lists
#     for i in aList:
#         tmp = i // placement
#         print("i is ", i)
#         print("placement is ", placement)
#         print("tmp is ", tmp)
#         print("tmp % RADIX is ", tmp % RADIX)
#         buckets[tmp % RADIX].append(i)
#         if maxLength and tmp > 0:
#             maxLength = False

#     # empty lists into aList array
#     a = 0
#     for b in range(RADIX):
#         buck = buckets[b]
#         for i in buck:
#             aList[a] = i
#             a += 1

#     # move to next digit
#     placement *= RADIX
#     return aList

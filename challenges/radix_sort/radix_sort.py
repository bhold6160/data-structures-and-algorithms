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

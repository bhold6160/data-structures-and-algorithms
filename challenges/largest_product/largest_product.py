def largest_product(arr):
    product = 0
    for i in range(len(arr)):
        if arr[i][0] * arr[i][1] > product:
            product = arr[i][0] * arr[i][1]
    return product
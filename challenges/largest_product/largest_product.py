def largest_product(new_list):
    counter = 0
    answer = 0
    new_list = []

    for item in new_list:
        new_list[counter] = item[0] * item[1]
    for answer in new_list:
        if answer < item:
            answer = item
    return answer
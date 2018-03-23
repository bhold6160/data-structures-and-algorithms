counter = 0
answer = 0

new_list = []
start_list = [[1, 2], [3, 4], [5, 6], [7, 8]]

def largest_product():
    for item in start_list:
        new_list[counter] = item[0] * item[1]
    for answer in new_list:
        if answer < item:
            answer = item
    return answer
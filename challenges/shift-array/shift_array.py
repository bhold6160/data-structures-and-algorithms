def insert_shift_array(arr, num):
    answer = [0] * (len(arr) + 1)
    middle = (len(arr) + len(arr) % 2) // 2

    for item in range(len(answer)):
        if item < middle:
            answer[item] = arr[item]
        elif item == middle:
            answer[item] = num
        else:
            answer[item] = arr[item - 1]
    return answer



def left_join(h1, h2):
    h1_counter = 0
    for item in h2.buckets:
        if item.head:
            h1_counter += 1
    if h1_counter == 0:
        return [x.head.val for x in h1.buckets]
    else:
        a = []
        for item in h1.buckets:
            temp = []
            if item.head:
                temp.append(list(item.head.val.keys())[0])
                temp.append(list(item.head.val.values())[0])

                num = h2.hash_key(list(item.head.val.keys())[0])
                if h2.buckets[num].head:
                    temp.append(list(h2.buckets[num].head.val.values())[0])
                else:
                    temp.append(None)
                a.append(temp)
        return a


# def psuedo_left_join(h1, h2):
#     """
#     Left joins two hashtables and returns combined list
#     """
#     combine = []

#     for key, value in h1:
#         temp = []
#         temp.append(key, value)
#         if key in h2:
#             temp.append(h2[key])
#         else:
#             temp.append('null')
#     combine.append(temp)
#     return combine

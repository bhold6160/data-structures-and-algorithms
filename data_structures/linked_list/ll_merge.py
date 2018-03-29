def merge_lists(ll_a, ll_b):
    ll_a = ll_a.head
    ll_b = ll_b.head
    a_next_node = ll_a.next
    b_next_node = ll_b.next

    while ll_a is not None and ll_b is not None:
        ll_a.next = ll_b
        if a_next_node is None:
            break
        ll_b.next = a_next_node
        ll_b = b_next_node
        b_next_node = ll_b.next
        ll_a = a_next_node
        if ll_a is not None:
            a_next_node = ll_a.next
    return ll_a

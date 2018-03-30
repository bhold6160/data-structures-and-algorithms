import shift_array as sa


def test_insert_shift_array():
    assert sa.insert_shift_array([1, 2, 3, 4], 40) == [1, 2, 40, 3, 4]

def test_empty_shift_array():
    assert sa.insert_shift_array([], 46) == [46]

from .merge_sort import merge_sort


def test_empty_merge_sort():
    """
    Test empty merge sort
    """
    assert merge_sort([]) == []


def test_merge_sort_with_one_int():
    """
    Test merge sort with one int
    """
    assert merge_sort([67]) == [67]


def test_merge_sort_with_many_ints():
    """
    Test merge sort with many ints
    """
    assert merge_sort([3, 6, 1, 81, 17, 9]) == [1, 3, 6, 9, 17, 81]


def test_merge_sort_uneven_amount_of_ints():
    """
    Test merge sort with uneven amount of ints
    """
    assert merge_sort([18, 37, 11, 90, 78]) == [11, 18, 37, 78, 90]
